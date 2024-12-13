# AdventOfCode-2024

## Language
Solutions will be completed in Python 3.13

## Goals
- Complete puzzles with no assistance
- Complete each puzzle daily through day 15 or higher
- Complete each day with an optimized runtime of < 1000ms

## Self Rules
1. No LLM/Copilot use
2. No looking at outside solutions (until I get a solution)

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


## Day 4
I lost track of time, and started late. I wrote a pretty basic, naive solution, that to my luck was really easy to convert to a solution for part 2! However, I had a really annoying bug on part 1, where I was incorrectly checking to see if a given position was out of bounds. This took me about 10 minutes to find, and was quite frustrating. I feel like I could have done a lot better, but after working to refine and optimize my code, I have a runtime of 11ms for parts 1 and 2 together, which I'm pretty happy with.

I also had some fun looking at other people's solutions (after finishing mine), and saw that you can actually use `j` as the imaginary number `i` to perform multiplication in Python. This can make cycling through lists of directions on the unit circle a lot easier, potentially.

Unfortunately, I fell on several of the AOC leaderboards I'm competing on due to my slow time today. Hopefully, I'll be able to pick it up tomorrow, and get some more fast times.


## Day 5
I was pretty happy with how I did today! I wrote some fairly simple logic using basic loops and comparing indices for part 1 that was enough to solve the part. For part 2, I sorted each incorrect list by swapping incorect elements until the list was sorted (swap sort). I'm sure that there's a more refined algorithm that could be used, but for now I'm happy with my solution.

I still haven't looked up others' solutions, and have not used an LLM for any of my code. And, I made it back to the sub 1000 ranks today!

## got lazy and didn't want to write

## Day 11
Part 1 was super easy- just a loop and some logic! I got it pretty quickly, but it took me some time to actually type out, and I think I started a minute late.

Part 2 was really hard- I tried a bunch of methods, including multiprocessing the brute force, but my laptop kept running out of memory! I also tried caching the forward paths for each stone, but this was incredibly slow, and again, laptop ran out of application memory (I have 48 GB). Then, I realized that all we care about is the number of stones, so we can do a DFS to find the number of stones, and by caching the result can make everything faster.

Also, while I was trying different solutions, I wrote out a quick function to count the number of digits using arithmetic. I don't know if this is actually faster, but it looks cooler, and I don't have to use janky string parsing for once.

I'm pretty happy that I got it in (almost) under 1 hour, and the runtime is fast! It could be even faster, but my solution for P1 ran with no bugs the first time I tried it, so I'm leaving it in there (the 58ms rute force solution could be cut to around 10ms if I used the smart solution). I did format and cleanup the code, though.

### Results Table (rank refers to global leaderboard)
| Day | Startup (ms) | Part 1 (ms) | Part 2 (ms) | Total (ms) | Part 1 Time | Part 2 Time |
| --- | ------------ | ----------- | ----------- | ---------- | ----------- | ----------- |
| 1   | 10.24        | 0.30        | 0.31        | 10.85      | 00:03:16    | 00:04:53    |
| 2   | 7.66         | 0.59        | 1.84        | 10.09      | 00:03:44    | 00:10:50    |
| 3   | 9.88         | 0.19        | 0.34        | 10.41      | 00:03:25    | 00:12:58    |
| 4   | 7.60         | 6.14        | 1.36        | 15.10      | 00:32:12    | 00:33:01    |
| 5   | 7.94         | 4.13        | 7.95        | 20.02      | 00:07:24    | 00:15:51    |
| 6   | 9.13         | 1.47        | 2453.42     | 2464.02    | 08:54:25    | 12:21:08    |
| 7   | 15.72        | 161.72      | 236.76      | 414.20     | 00:12:28    | 00:14:53    |
| 8   | 12.18        | 0.48        | 0.27        | 12.93      | 21:46:04    | 22:43:23    |
| 9   | 8.67         | 6.17        | 7.42        | 22.26      | 00:25:04    | 01:12:45    |
| 10  | 7.95         | 3.44        | 2.71        | 14.10      | 00:37:06    | 00:39:18    |
| 11  | 9.51         | 58.12       | 27.08       | 94.71      | 00:06:40    | 01:08:03    |
| 12  | 9.19         | 17.71       | 24.01       | 47.91      | 00:22:57    | 20:17:40    |


** I write each part to execute separately. Even if it would be faster to solve both parts simultaenously, I'm choosing to evaluate them separately. Runtimes are evaluated on M4 Pro MacBook Pro