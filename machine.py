from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
import os
pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'sub-c-52efa958-798f-11e8-bf64-d6949d01620d'
pnconfig.publish_key = 'pub-c-6d4ea8c5-03f9-4f92-bb89-cceec7eaadea'

pubnub = PubNub(pnconfig)

channel = 'ch'

class Listener(SubscribeCallback):
	def message(self, pubnub, message):
		print(message.message)
		if "play:" in message.message:
			file = message.message[5:]
			os.system('pkill aplay')
			os.system('aplay' + ' /home/pi/Projects/NoiseMachine/sounds/' + file + ' &'); 

print('Listening...')
pubnub.add_listener(Listener())
pubnub.subscribe().channels(channel).execute()