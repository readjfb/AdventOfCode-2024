# AdventOfCode-2024

## Language
Solutions will be completed in Python 3.13

## Goals
- Complete puzzles with no assistance
- Complete each puzzle daily through day 15 or higher
- Complete each day with an optimized runtime of < 1000ms

## Self Rules
1. No LLM/Copilot use
2. No looking at outside solutions for the first hour(s) of effort

# Journal (Spoiler Alert)

## Day 1
This day was pretty straightforward- except the three spaces between the two numbers in the lists caused my `.split(" ")` to generate extra entries in the middle, which messed up my parsing at first. This cost me about 30 seconds to realize. After that, it was a simple matter of sorting lists, and iterating through them

For the second part, I used the Counter module. I found out about this last year, and while I haven't used it for anything in a real project or work, it's very helpful when you need to just count a bunch of entries in a list. All in all, pretty straightforward in Python.

I didn't have to optimize this much at all, just cleaned up some syntax. Both parts 1 and 2 run in 1ms, the majority of which is splitting the inputs.

## Day 2
This day was pretty fun- I started writing a dynamic programming solution to identify if the ranges were couning up or down, but when I glanced over and saw that there were only 1000 rows in the input, I wrote a quick and dirty brute force solution.

I was able to reuse almost all of my code from part 1 on part 2, and (though I'm not proud of it) just tried out removing each element sequentially until I found something that was "Safe."

I then had some fun optimizing my code- initially, both parts combined to take almost 100ms to run, but after optimization, both parts together take 8ms! Part 1 takes 2 ms, and part 2 takes 6ms. I found out that the python `all()` function takes longer in some instances than just looping manually, so I was able to shave off about 10ms by writing out the loops

## Day 3
I didn't use an LLM! That being said, my regex skills are rusty. I used the [regex101](https://regex101.com) website to help me write my query. I would have had an answer far quicker, but forgot that `()` were special characters in regex, and remembering to add the escape character `\` took a bit of time. I also somehow managed to only select half of my puzzle input at first, which took me almost a minute to realize.

I hadn't used the `|` (or) command in Python regex extensively before, and didn't expect it to output a tuple with the different capture groups. This took me some time to figure out, and so this combined with not realizing that the example for part 2 was different to make my time a bit longer than it needed to be. With that being said, I'm proud that I was able to come up with the regex commands on my own and in a reasonable amount of time.

Regex is really fast though; both part 1 and part 2 only take 1ms to run.


### Results Table (rank refers to global leaderboard)
| Day   | Part 1 Time | Part 1 Rank | Part 1 Runtime (ms) | Part 2 Time | Part 2 Rank | Part 2 Runtime (ms) |
| ----- | ----------- | ----------- | ------------------- | ----------- | ----------- | ------------------- |
| Day 1 | 00:03:16    | 903         | 1                   | 00:04:53    | 719         | 1                   |
| Day 2 | 00:03:44    | 203         | 2                   | 00:10:50    | 961         | 6                   |
| Day 3 | 00:03:25    | 717         | 1                   | 00:12:58    | 1784        | 1                   |

**I did use an LLM to generate this markdown table, because why not