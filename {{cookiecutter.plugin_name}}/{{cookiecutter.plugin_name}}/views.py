from formshare.plugins.utilities import formSharePublicView,formSharePrivateView

class myPublicView(formSharePublicView):
    def processView(self):
        return {}

class myPrivateView(formSharePrivateView):
    def processView(self):
        return {}