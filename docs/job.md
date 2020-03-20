# Job

A job defines work that needs to be done by the client.  Jobs are stored in the server and communicated to a client when the `get_work` endpoint is called.

## JSON definition

A job is communicated as a simple JSON object where key names and values are lower case:

* `job_type`: This value indicates which endpoint the job refers to.  Possible values are:
  * `documents`
  * `document`
  * `docket`
  * `download`
  * `none` - used to indicate that there is no work to be done.
* `url`: The url for the job.  This url should contain the server name, path to the end point, and all parameters **except** the API key.


## Examples

```
{
  'job_type': 'document',
  'url': 'https://api.data.gov/regulations/v3/document.json?documentId=EPA-HQ-OAR-2011-0028-0108'
}  
