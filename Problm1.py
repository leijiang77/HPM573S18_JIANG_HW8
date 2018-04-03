

import classes as Cls
import scr.FigureSupport as figureLibrary
import scr.FormatFunctions as Format
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.StatisticalClasses as Stat

# Calculate expected reward of 1000 games
trial = Cls.SetOfGames(id=1,prob_head=0.5, n_games=1000)
test=trial.simulation()

trial2=Cls.SetOfGames(id=2,prob_head=0.45,n_games=1000)
test2=trial2.simulation()


# print outcomes of each cohort
print("The expected reward is",test.get_ave_reward(), 'when probability of head is 0.5 and' ,
      "The 95% CI of expected reward is:", test.get_CI_reward(0.05))
print("The expected reward is",test2.get_ave_reward(), 'when probability of head is 0.45 and' ,
      "The 95% CI of expected reward is:", test2.get_CI_reward(0.05))


increase = Stat.DifferenceStatIndp(
        name='Increase in reward',
        x = test2.get_rewards(),
        y_ref=test.get_rewards()
    )


estimate_CI = Format.format_estimate_interval(
    estimate=increase.get_mean(),
    interval=increase.get_t_CI(alpha=0.05),
    deci=1
)
print("Average increase in reward is and confidence interval is", estimate_CI)


