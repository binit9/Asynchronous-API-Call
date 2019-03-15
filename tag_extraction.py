
import os
from tika import parser

def extract_tag(req_json):
    filename = req_json['filename']
    trxid = req_json['transaction_id']
    type_,content = extract_content(filename)
    
    if type_ == "supported":
        text_,policy_content = extract_policies(content)
        
        if text_ == "supported":
            return {"Status": "OK",
                    "Message": "Tag Extraction Successful",
                    "error code": "",
                    "respObj":{
                        "source": "accentureai",
                        "transaction_id": trxid,
                        "AI_Output":
                            {"content":policy_content}
                            }}
        
        elif text_ == "unsupported":
            return {"Status": "KO",
                    "Message": " Unsupported Text Format",
                    "error code": "",
                    "respObj":{
                        "source": "accentureai",
                        "transaction_id": trxid,
                        "AI_Output":{"content":[]}
                    }}
        
    elif type_ == "unsupported":
        return {"Status": "KO",
                "Message": " Invalid File Extension",
                "error code": "",
                "respObj":{
                    "source": "accentureai",
                    "transaction_id": trxid,
                    "AI_Output":{"content":[]}
                }}

    
    
def extract_content(file):
    content = []
    if file.endswith(('pdf','doc','docx')):
        filetype = "supported"
        # Parse data from file
        file_data = parser.from_file(file)
        # Get files text content
        text = file_data['content']
        indexes = [i for i,x in enumerate(text.split('\n')) if x == '###' or x == '### ']
        content.append((indexes,text.split('\n')))
    else:
        filetype = "unsupported"
        content =[]
        

    return filetype,content

def extract_policies(content_docs):
        
        lst = []
        for doc in content_docs:
            indexes= doc[0]
            print(indexes)
            policies_list = []
            if len(indexes) != 0:
                for i in range(len(indexes)):
                    if i == len(indexes)-1:
                        policies_list.append(doc[1][indexes[i]+1:])
                    else:
                        policies_list.append(doc[1][indexes[i]+1:indexes[i+1]])
                lst.append(policies_list)
                text_format = "supported"
            else:
                lst.append([]) 
                text_format = "unsupported"
                
        return text_format,lst
