import classes as Cls
import scr.StatisticalClasses as Stat
import scr.FormatFunctions as Format

# create a multiple game sets
multipleGameSets=Cls.MultipleGameSets(ids=range(1000), prob_head=0.5, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets.simulation()


multipleGameSets2=Cls.MultipleGameSets(ids=range(1000), prob_head=0.45, n_games_in_a_set=10)
# simulate all game sets
multipleGameSets2.simulation()

# print projected mean reward
print('Projected mean reward',
      multipleGameSets.get_mean_total_reward(),'with 95% projection interval of average rewards',
      multipleGameSets.get_PI_total_reward(0.05),"with head probability of 0.5")

print('Projected mean reward',
      multipleGameSets2.get_mean_total_reward(),'with 95% projection interval of average rewards',
      multipleGameSets2.get_PI_total_reward(0.05),"with head probability of 0.45")

increase = Stat.DifferenceStatIndp(
    name='Increase in mean survival time',
    x=multipleGameSets2.get_mean_reward(),
    y_ref=multipleGameSets.get_mean_reward()
)
# estimate and prediction interval
estimate_CI = Format.format_estimate_interval(
    estimate=increase.get_mean(),
    interval=increase.get_PI(alpha=0.05),
    deci=1
)

print("Expected increase in mean reward and prediction interval is",estimate_CI)

