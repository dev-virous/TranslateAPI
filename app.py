from flask import Flask, request
from translator import Translator
from json import dumps
app = Flask(__name__)

#{
#	"developer": "t.me/V_IRUuS"
#}

def get_args(request):
	if request.method == "GET":
		query = request.args.get("query")
		from_lang = request.args.get("query.source_language")
		to_lang = request.args.get("query.target_language")
	else:
		query = request.json.get("query")
		from_lang = request.json.get("query.source_language")
		to_lang = request.json.get("query.target_language")
	return query, from_lang, to_lang

@app.route("/translator", methods=["GET", "POST"])
def translator():
	query, from_lang, to_lang = get_args(request)
	if not query:
		data = {
			"success": False,
			"Exception": {
				"code": 400,
				"ErrorMsg": "Request contains an invalid argument.",
			}
		}
		return dumps(data, indent=4, ensure_ascii=False), 400, {"Content-Type": "application/json; charset=utf-8"}
	elif not to_lang:
		data = {
			"success": False,
			"Exception": {
				"code": 400,
				"ErrorMsg": "Request contains an invalid argument.",
			}
		}
		return dumps(data, indent=4, ensure_ascii=False), 400, {"Content-Type": "application/json; charset=utf-8"}
	else:
		try:
			client = Translator(
				from_lang=from_lang,
				to_lang=to_lang
			)
			translate = client.translate(query)
			data = {
				"success": True,
				"sentences": {
					"trans": translate,
					"original": query,
				}
			}
			if not from_lang:
				data["sentences"]["detection_lang"] = client.from_lang
			return dumps(data, indent=4, ensure_ascii=False), {"Content-Type": "application/json; charset=utf-8"}
		except Exception as ErrorMsg:
			data = {
				"success": False,
				"Exception": {
					"code": 400,
					"ErrorMsg": str(ErrorMsg),
				}
			}
			return dumps(data, indent=4, ensure_ascii=False), 400, {"Content-Type": "application/json; charset=utf-8"}

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
		port="8080"
	)