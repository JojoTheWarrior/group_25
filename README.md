# Stack
- Set up a Django endpoint that you can ping to run the solver, hosted on GCP
- Use multiprocessing in Python to simultaneously iterate over different flush selections
- Have some data structure of "all valid histograms" as a Python tree
- Make a website where you can play the game using HTML+CSS+JS

# Algorithm
- Precompute all valid histograms and store them into a tree
- Enumerate over flush picks, and travel the tree for each remaining set to see if it works

# Encoding and Decoding Enumerations
- When we generated the tree of all valid histograms, how many different selections did we have to go through? Consider the most extreme case when out of the 321 pieces, we're choosing 5 of them (with rep). There are 325C4 $\approx$ 450 million such selections. To enumerate over selections, we can use an encryption system where $Rank(a_1 < a_2 < ... < a_4)= \sum_{i=1}^4 \binom{a_i}{i}$.