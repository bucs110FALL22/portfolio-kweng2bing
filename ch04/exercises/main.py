article = "Yes. Some public health officials are strongly recommending getting both the flu shot and the new bivalent booster at once — Dr. Asish Jha, who leads the White House’s pandemic response, remarked in a press briefing that “God gave us two arms: one for the flu shot and the other one for the Covid shot.” Combining vaccines, in general, is not unusual: children often receive multiple shots at once, said Dr. Peter Chin-Hong, an infectious disease specialist at the University of California, San Francisco. And getting two shots at the same time means you’re less likely to forget, or put off, either one, he added. “Convenience trumps everything,” he said. Most people will want to get one shot in each arm, Dr. Chin-Hong said, but you can receive both vaccines in the same arm — you just might be extra sore. “It’s personal preference — there’s no medical reason to do it one way or another,” said Dr. Adam Ratner, a pediatric infectious disease specialist at N.Y.U. Langone. People who opt for two vaccines at once might experience more side effects, which are similar for both shots: tenderness at the injection site, headaches, fatigue. A small number of people may develop a fever. If you want to spread out your shots, you may want to schedule your flu shot for later in the fall, so that protection from the vaccine kicks in when cases begin to rise in the winter. You can also monitor flu activity in your state, through the Centers for Disease Control and Prevention’s influenza surveillance reports, to assess whether you want to get the shot now or later. You're almost out of free articles. "
# print(article)
replace = {
  "covid":"heaven",
  "flu": "nothing",
  "shot":"drink",
  "Dr.": "Comedian,",
  "rise": "normal",
  "health":"happiness",
  "booster": "water",
  "medical": "MONEY",
  "disease": "anime",
  "pandemic": "fireworks"
}
newArticle = []
for i in article.split( ):
  newArticle.append(replace.get(i,i))
  # print(i)
  # print(newArticle)
newArticle= ' '.join(newArticle)
print(newArticle)

# https://www.nytimes.com/article/covid-booster-flu-shot-same-time.html