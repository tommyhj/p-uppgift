class TV:


	def __init(self, file):
		self.volume = volume
		self.channels = ["MTv: Music is life", "Tv 3: Har du tur i kärlek?","Svt 1: Pengar är inte allt","Kanal 4: Vem vill inte bli miljonär?"]
		self.channel = channels[0]

	def set_channel(self, channel):
		channel -= 1
		if (channel) >len(channels) and channel < 0:
			return "fail"
		else:
			self.channel = self.channels[channel]

	def get_channel(self):
		return self.channel

	def set_volume(self, volume):
		self.volume = volume
	
	def get_volume(self):
		return volume