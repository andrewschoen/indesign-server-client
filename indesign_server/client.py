from suds.client import Client

class InDesignServerClient(object):
    def __init__(self, wsdl, host=None, timeout=90):
        """
        Create a new connection to InDesign Server

        Parameters
        __________
        wsdl
            The URI of the InDesign Server wsdl file.  
            (e.g. "http://localhost:18383/service?wsdl")
        host
            The URI of the targeted instance of InDesign Server.  If not 
            specified, the host URI is defined by the "SOAP:address location="
            section of the wsdl.
        timeout
            Time, in seconds, to give HTTP requests to complete.
        
        """
        self.client = Client(wsdl)
        if host:
            self.client.set_options(location=host)
        if timeout:
            self.client.set_options(timeout=timeout)

    def run_script(self, script_file, script_language, script_text=None,
             script_args=None):
        """
        Executes the RunScript method of the InDesign Server SOAP service.

        Parameters
        __________
        script_file
            The path to the script to execute.  The path is based on the 
            file system of the targeted InDesign Server instance.
        script_language
            The language used to program the script:  "javascript", 
            "visual basic", or "applescript"
        script_text
            Script to run if no script_file is specified
        script_args
            A dict containing the arguments to the script. Example:
            params = {"arg0":100, "arg1":"This is some text."}

        """
        params = {}
        params.update({
            "scriptLanguage":script_language,
            "scriptFile":script_file,  
        })
        if script_text:
            params.update({"scriptText":script_text})
        if script_args:
            args = [{"name":k, "value":v} for k, v in script_args.iteritems()]
            params.update({"scriptArgs":args})
        result = self.client.service.RunScript(params)
        return result

        