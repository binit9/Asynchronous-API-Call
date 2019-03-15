# Asynchronous-API-Call

A python service for asynchronous API call. A multi-level request response system in which a longer task runs in the background. U may request status of the task any time. 

Python / AI service will be exposed via asynchronous REST API services with Request and Response in JSON format.
The API call is asynchronous in nature and therefore, there are 2 levels of responses:
	Acknowledgement response indicating the successful receipt of the initial request.
	Final response indicating the status and result in response to the status request.

Both the requests expect transaction ID. Both the responses contain the transaction ID too for the identification of the transaction. 
There is another level of identification – Task ID which works internally to fetch the status of the task. The user need not mention this id on request or status JSONs.
