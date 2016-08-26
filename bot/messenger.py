import logging
import random

import requests
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)

def make_pie( df, column ):
	counts = pd.DataFrame(df[column].value_counts())

	plot = counts.plot.pie(y=column)
	fig = plot.get_figure()
	plt.show()

def make_bar( df, column ):
	counts = pd.DataFrame(df[column].value_counts())

	plot = counts.plot.bar(y=column)
	fig = plot.get_figure()
	plt.show()

def make_scatter( df, x_axis, y_axis):
	dfplot = df.plot.scatter(x=x_axis, y=y_axis)
	fig = dfplot.get_figure()
	plt.show()

def make_box( df, column ):
	if column not in df:
		plot = df.plot.box()
	else:
		plot = df.plot.box(y=column)

	fig = plot.get_figure()
	plt.show()


class Messenger(object):
    def __init__(self, slack_clients):
        self.clients = slack_clients

    def send_message(self, channel_id, msg):
        # in the case of Group and Private channels, RTM channel payload is a complex dictionary
        if isinstance(channel_id, dict):
            channel_id = channel_id['id']
        logger.debug('Sending msg: {} to channel: {}'.format(msg, channel_id))
        channel = self.clients.rtm.server.channels.find(channel_id)
        channel.send_message("{}".format(msg.encode('ascii', 'ignore')))

    def write_help_message(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = '{}\n{}\n{}\n{}'.format(
            "I'm your friendly Slack bot written in Python.  I'll *_respond_* to the following commands:",
            "> `hi <@" + bot_uid + ">` - I'll respond with a randomized greeting mentioning your user. :wave:",
            "> `<@" + bot_uid + "> joke` - I'll tell you one of my finest jokes, with a typing pause for effect. :laughing:",
            "> `<@" + bot_uid + "> attachment` - I'll demo a post with an attachment using the Web API. :paperclip:")
        self.send_message(channel_id, txt)

    def write_greeting(self, channel_id, user_id):
        greetings = ['Hi', 'Hello', 'Nice to meet you', 'Howdy', 'Salutations']
        txt = '{}, <@{}>!'.format(random.choice(greetings), user_id)
        self.send_message(channel_id, txt)

    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "I'm sorry, I didn't quite understand... Can I help you? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_joke(self, channel_id):
        question = "Why did the python cross the road?"
        self.send_message(channel_id, question)
        self.clients.send_user_typing_pause(channel_id)
        answer = "To eat the chicken on the other side! :laughing:"
        self.send_message(channel_id, answer)


    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: my maker didn't handle this error very well:\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)

    def demo_attachment(self, channel_id):
        txt = "Beep Beep Boop is a ridiculously simple hosting platform for your Slackbots."
        attachment = {
            "pretext": "We bring bots to life. :sunglasses: :thumbsup:",
            "title": "Host, deploy and share your bot in seconds.",
            "title_link": "https://beepboophq.com/",
            "text": txt,
            "fallback": txt,
            "image_url": "https://storage.googleapis.com/beepboophq/_assets/bot-1.22f6fb.png",
            "color": "#7CD197",
        }
        self.clients.web.chat.post_message(channel_id, txt, attachments=[attachment], as_user='true')

    def graph(self, channel_id):
        txt = "Now we're gonna send you back a graph!"
        self.send_message(channel_id, txt)
    def same(self, channel_id, msg):
        self.send_message(channel_id, msg)
    def process_csv(self, channel_id, msg):
        r = requests.get(str(msg.encode('utf-8'))[1:-1])
        #contents = str(r.text.encode('utf-8'))
        soup = BeautifulSoup(r.text)
        res = soup.find("div", {"class":"CodeMirror-code"})
        pre = res.find_all('pre')
        #msg = str(pre[0].encode('utf-8'))[5:-6]
        
        with open('csv.csv', 'wt') as out_file:
            for line in pre:
                out_file.write(str(line.encode('utf-8'))[5:-6])

        ####### DEFINE THE CSV TO READ FROM ########
        #df = pd.read_csv("./csv.csv")
        
        ####### GET COLUMNS #########
        #columns = list(df.columns.values)
        #print "columns in dataframe: " + str(columns)
        
        
        #print "available plot types ['bar', 'barh', 'box', 'density', 'hexbin', 'hist', 'kde', 'line', 'pie', 'scatter']"

        # plot shit goes here

        

        #self.send_message(channel_id, 'j')
        attachment = {
            "pretext": "We bring bots to life. :sunglasses: :thumbsup:",
            "title": "Host, deploy and share your bot in seconds.",
            "title_link": "https://beepboophq.com/",
            "text": txt,
            "fallback": txt,
            #"image_url": "https://storage.googleapis.com/beepboophq/_assets/bot-1.22f6fb.png",
            "image_url": "josh.png",
            "color": "#7CD197",
        }
        self.clients.web.chat.post_message(channel_id, 'j', attachments=[attachment], as_user='true')
    
