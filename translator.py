from requests import session
from fake_useragent import UserAgent

#{
#	"developer": "t.me/V_IRUuS"
#}

class Translator:
	def __init__(
		self,
		from_lang=None,
		to_lang=None
	):
		self.session = session()
		self.UserAgent = UserAgent().random
		self.from_lang = from_lang
		self.to_lang = to_lang
		headers = {
			"User-Agent": self.UserAgent
		}
		self.session.headers.update(headers)
	def detect(
		self,
		query
	):
		data = {
			"text_to_translate": str(query)
		}
		language = self.session.post("https://www.translate.com/translator/ajax_lang_auto_detect", data=data).json()["language"]
		return language
	def translate(
		self,
		query,
	):
		if not self.from_lang:
			self.from_lang = self.detect(query)
		params = {
			"client": "dict-chrome-ex",
			"sl": self.from_lang,
			"tl": self.to_lang,
			"dt": "t",
			"q": query
		}
		sentences = self.session.get("https://translate.google.com/translate_a/t", params=params).json()
		return sentences