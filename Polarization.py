import twint
import nest_asyncio

nest_asyncio.apply()

c = twint.Config()
c.Search = "#RBG"
c.Store_json = True
c.Limit = 50000
c.Output = 'RBG.json'
twint.run.Search(c)