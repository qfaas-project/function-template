# Function Template

Function templates and the synthetic function examples

## Prerequisites

- The way of using `faas-cli` to build a OpenFaaS function image
	- Offcial example: https://github.com/openfaas/python-flask-template
- In short, a functiom image is a combination of: `request handler` + `language runtime` + `function code`. In OpenFaaS
	- `request handler` is the `of-watchdog` ([qfaas of-watchdog](https://github.com/qfaas-project/of-watchdog))
	- `language runtime` is the function `template` (this repo)


## Example

Here is an example to build a qfaas python function image

Please check the `Dockerfile` in each template to get more information

```
cd single-function/python
faas-cli build -f fun-py-flask-qfaas.yml
# > faas deploy -f fun-py-flask-qfaas.yml # change the gateway IP:Port in yml file first
# or > faas deploy -g IP:Port -f fun-py-flask-qfaas.yml
```  

*More templates comming soon...*
