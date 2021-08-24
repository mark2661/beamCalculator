from BEAM.Support.Support import Support


class RollerSupport(Support):

    def __init__(self, location, vertical_reaction=None):
        Support.__init__(self, location, "roller", vertical_reaction)
