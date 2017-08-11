import abjad
from calliope import tools, bubbles, machines

class ClusterNode(bubbles.Bubble):
    leaf_string="c'4"
    def __init__(self, leaf_string=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if leaf_string:
            self.leaf_string = leaf_string

class Cluster(bubbles.Bubble):
    container_type = abjad.Cluster
    is_simultaneous = False
    sub_types = (ClusterNode, )

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.extend( [ClusterNode(arg) for arg in args] )

    def child_music(self, child_bubble):
        return abjad.Chord(child_bubble.leaf_string)

class Cluster1(Cluster):
    start = ClusterNode("<c' a''>2.")
    middle = ClusterNode("<g' d''>4")
    end = ClusterNode("<a' b'>4")

class Clusters(bubbles.Bubble):
    cluster_types = ()
    is_simultaneous = False
    times =1

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        if args:
            self.cluster_types = args
        # print( self.cluster_types[0]().ly() )
        self.extend( [c()() for c in self.cluster_types] )

class DemoBubble(machines.LineBlock):
    clusters_I = Clusters(
        Cluster1,
        Cluster1(middle=ClusterNode("c'''4")),
        Cluster1,
        )


tools.illustrate_me( bubble=DemoBubble )


# class ScoreDemo(bubbles.Score):

#     class Flute(bubbles.Staff):
#         instrument=abjad.instrumenttools.Flute(
#             instrument_name="Flute", short_instrument_name="fl.")

#     class Clarinet(bubbles.Staff):
#         instrument=abjad.instrumenttools.ClarinetInBFlat(
#             instrument_name="Clarinet in Bb", short_instrument_name="cl.")

#     class MyStaffGroup(bubbles.StaffGroup):
#         class Violin1(bubbles.Staff):
#             instrument=abjad.instrumenttools.Violin(
#                 instrument_name="Violin 1", short_instrument_name="vln.")

#         class Violin2(bubbles.Staff):
#             instrument=abjad.instrumenttools.Violin(
#                 instrument_name="Violin 2", short_instrument_name="vln.")



# ==============================================

# tools.illustrate_me(  )