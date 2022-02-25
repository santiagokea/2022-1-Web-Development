from bottle import default_app, delete, get, post, put, request, response, run, view
import g
import uuid
import time

# print("#"*30)
# print(dir(time))
# print(int(time.time()))



tweets = {}

##############################
@post("/tweets")
def _():
  # Validate
  if not request.forms.get("tweet_text"):
    response.status = 400
    return "tweet_text missing"

  tweet_text = request.forms.get("tweet_text").strip()
  
  if len(tweet_text) < g.TWEET_MIN_LEN:
    response.status = 400
    return f"tweet min {g.TWEET_MIN_LEN}"

  if len(tweet_text) > g.TWEET_MAX_LEN:
    response.status = 400
    return f"tweet max {g.TWEET_MAX_LEN}"

  tweet_id = str(uuid.uuid4())
  tweet_created_at = int(time.time())
  tweet = {
    "tweet_id" : tweet_id,
    "tweet_text" : tweet_text,
    "tweet_created_at" : tweet_created_at
  }
  tweets[tweet_id] = tweet

  # Success  
  return {"info":f"New tweet created with id {tweet_id}"}

##############################
@put("/tweets/<id>")
def _(id):
  return "tweet updated"

##############################
@delete("/tweets/<id>")
def _(id):
  return "tweet deleted"

##############################
@get("/tweets/<id>")
def _(id):
  return "this is the tweet"

##############################
@get("/tweets")
def _():
  return tweets


##############################
try:
  # Production
  import production
  application = default_app()
except:
  # Development
  run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")






