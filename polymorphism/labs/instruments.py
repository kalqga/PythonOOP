class Guitar:
    def play(self):
        print("playing the guitar")


def play_instrument(ins):
    return ins.play()


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
play_instrument(piano)

guitar = Guitar()
play_instrument(guitar)
