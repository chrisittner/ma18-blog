title: GSoC Project Outline

The following project description is taken from my proposal _Structure learning from complete data for pgmpy_ for Google Summer of Code 2016. The timeline below is preliminary and will be updated as needed. The GSoC work period is May-August.

# The Project

I will introduce methods to pgmpy to select Bayesian models based on data sets. First, I'll implement basic support for score-based and constraint-based structure learning. Second, I will add common enhancements to the score-based approach, including local score computation + memoization and tabu lists. Finally, I will implement the MMHC algorithm, which combines the score-based and the constraint-based method.

## Motivation

By now, pgmpy supports most of the fundamental operations on probabilistic graphical models (PGMs). Given a data set and a suitable Bayesian network model, pgmpy can parametrize the model based on the data and perform the usual array of inference and sampling tasks. But the model itself must still be supplied manually.

Selecting appropriate models is a major challenge in the application of graphical models. Manual construction of e.g. Bayesian networks is error-prone and infeasible for large models. “Does variable X _directly_ influence Y, or might they have a common cause?” Questions like these should be answered based on data, where possible.

Algorithmic structure learning is an essential feature for any PGM library. In addition, here are two reasons why pgmpy in particular should seek to support structure learning now:

- Structure learning is currently the missing piece for the full PGM data analysis toolchain in pgmpy. Once this feature is implemented, pgmpy can be used for inference and sampling tasks, starting from a data set alone. This will be helpful to convince new users to work with pgmpy. It aids to open pgmpy to a wider audience of data scientists that are not familiar with the internals of causal modeling.
- Structure learning is a recent topic of interest in PGM research. pgmpy has an easily extensible code structure and (aims to have) pythonic implementations. These features make pgmpy a valuable tool to both, researchers and students, who want to experiment with (modified) PGM algorithms. [This](http://www.amazon.com/Mastering-Probabilistic-Graphical-Models-Python/dp/1784394688) book is a recent example of the educational nature of the library. pgmpy should not miss its chance to grow as an instructive resource and should seek to cover trending topics such as structure learning as soon as possible.

## Scope
Techniques for structure learning differ for Bayesian networks and Markov networks, and depending on whether or not the data is complete (In the sense that (i) each data sample contains information about exactly the same set of variables and (ii) no relevant variables are hidden). In this project, I will implement structure learning for Bayesian models and complete data.

I will add two model selection techniques to pgmpy: score-based model selection and constraint-based model selection. In addition to these basic approaches, I will implement a combination of the two, the MMHC algorithm proposed in [[Tsamardinos et al.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.4729&rep=rep1&type=pdf), 2006].

Below, I briefly describe the score-based and constraint-based approach, as well as the MMHC algorithm.

#### Score-based model selection

This approach construes model selection as an optimization task. It has two building blocks:

- A _scoring function_ $s_D\colon M \to \mathbb R$ that maps models to a numerical score, based on how well they fit to a given data set $D$.
- A _search strategy_ to traverse the search space of possible models $M$ and select a model with optimal score.

In the case of Bayesian network models, there are two natural candidates for the search space: the set of all Directed Acyclic Graphs (DAGs) or the set of all DAG patterns (I-equivalence classes of DAGs). In order to support search on both, I will add a representation for DAG patterns to pgmpy.

##### Scoring functions
Two common scores to measure the fit between model and data are the _Bayesian Dirichlet score_ and the _Bayesian Information Criterion_ (BIC, also called MDL). I will provide implementations for BDe(u) and K2 (two instances of the Bayesian Dirichlet score), and for the BIC score.

Importantly, these scores _decompose_, i.e. they can be computed locally for each of the variables, independent of other parts of the network. The score implementation will support memoization, such that local scores are only computed once.

##### Search strategies
The search space of DAGs or DAG patterns is super-exponential in the number of variables and the typical scoring functions allow for local maxima. The first property makes exhaustive search intractable for all but very small networks, the second prohibits efficient local optimization algorithms to always find the optimal structure. Thus, all interesting search strategies are heuristic.

I want to implement the following heuristic search strategies:

- Greedy Equivalence Search for DAGs and DAG patterns
- First ascent hill climbing for DAGs (see [PGM09, page 814f]), with enhancements:
  - Use tabu lists to ensure that new structures are explored
  - Use score decomposition effectively

And for the sake of completeness:

  - Exhaustive search for DAGs and DAG patterns


#### Constraint-based model selection

A common alternative approach to construct models is the following:
1. Identify independencies in the data set using hypothesis tests
2. Construct DAG (pattern) according to identified independencies

There are polynomial-time algorithms for model construction from a set of independencies (see [[LBN04](http://www.cs.technion.ac.il/~dang/books/Learning%20Bayesian%20Networks&#40;Neapolitan,%20Richard&#41;.pdf), page 550] for pseudocode of the PC algorithm, that was introduced by [[Spirtes et al.](https://mitpress.mit.edu/books/causation-prediction-and-search), 1993]). These algorithms are generally more efficient than score-based methods but only work under the assumption that the set of independencies is _faithful_, i.e. there exists a DAG that exactly corresponds to it. Spurious dependencies in the data set can cause the reported independencies to violate faithfulness. The faithfulness requirement also makes it difficult to construct a Bayesian network from a manually provided list of independencies, because that list must first be extended to satisfy the faithfulness criterion. This in turn is computationally unfeasible except for small models. I will implement constraint-based model selection using independence tests from `scipy.stats` and the PC model construction algorithm.

#### The MMHC algorithm

The MMHC algorithm combines the constraint-based and score-based method effectively. The authors suggest in [[Tsamardinos et al](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.4729&rep=rep1&type=pdf), 2006] that it performs very well against other state-of-the-art structure finding algorithms. At the same time, it is not too difficult to implement. It has two basic steps:

- Learn undirected graph skeleton using independence tests + constraint-based construction procedure
- Orient edges using score-based optimization with Bayesian score + modified hill-climbing search


# Timeline

The GSoC period will be structured in 6 bi-weekly milestones. Each milestone begins with a discussion post on the GSoC blog.

## Milestone 1: Scoring methods

#### Implement representation for DAG patterns (= I-Equivalence class of DAGs)

Add base class for DAG pattern similar to `DirectedGraph`, except that some edges are undirected. The implementation might use a networkx `MultiDiGraph`, with arrows in both directions for undirected edges (then DAG instances are actual subgraphs of the pattern) or an `UndirectedGraph` + a list of v-structures, depending on which performs better. Add methods to get DAG pattern from `DirectedGraph` and to construct `DirectedGraph` from DAG pattern (there is an easy algorithm for that in [[LBN04](http://www.cs.technion.ac.il/~dang/books/Learning%20Bayesian%20Networks&#40;Neapolitan,%20Richard&#41;.pdf), etc.]).

#### Implement Bayesian score and BIC score

Since there are multiple scoring methods with common structure, they will derive from a common abstract class. The base class takes a data set as a parameter and exposes a score-method. If the score is decomposable, a local_score method is public as well.

The Bayesian score for a model $m$, given a data set $D$ is essentially the (marginal) likelihood $P(m|D)$. See [PGM09, sections 18.3.2-18.3.6] or [these slides](https://www.cs.helsinki.fi/u/bmmalone/probabilistic-models-spring-2014/ScoringFunctions.pdf) for a derivation of the scores. The implementation will support Bayesian Dirichlet priors, in particular the so-called BDe(u) and K2 score. The K2 score, for example, is given by the following term:

$$score^{K2}_D(m) = \log(P(m)) + \sum_{X\in nodes(m)} local\_score^{K2}_D(X, parents_m(X))$$

where $P(m)$ is some optional structure prior. $local\_score^{K2}$ is computed for each node as follows (see [[Lerner&Malka](http://www.ee.bgu.ac.il/~boaz/LernerMalkaAAI2011.pdf), 2011, apply $\log$ to their equation 3]):

$$local\_score^{K2}_D(X, P_X) = \sum_{j=1}^{q(P_X)} (\log(\frac{(r-1)!}{(N_j+r-1)!}) + \sum_{k=1}^r \log(N_{jk}!))$$

Where $r$ is the cardinality of the variable $X$, $q(P_X)$ is the product of the cardinalities of the parents of $X$ (= the possible states of $P_X$) and $N_{jk}$ is the number of times that variable $X$ is in state $k$ while parents are in state $j$ in the data sample. Finally, $N_j:=\sum_{k=1}^r N_{jk}$.

The BDe(u) and BIC score can similarly be computed from some closed equation. All methods will be implemented to score both DAGs and DAG patterns.


## Milestone 2: Work on estimators, structure search

#### Split estimator base classes

The BaseEstimator class will be split in one `ParameterEstimator` and one `StructureEstimator` base class, so that they can each define a common interface for derived classes. `ParameterEstimator` is initialized with a data set and a model and should minimally expose `get_parameters` (and maybe `get_parameter` if the estimator decomposes). A `StructureEstimator` is initialized with a data set and minimally exposes `get_model`.

#### Port `BayesianEstimator` from `book/v0.1` branch
Add support for Bayesian parameter estimation. Currently pgmpy has ML parameter estimation, which [overfits](https://en.wikipedia.org/wiki/Overfitting) the data. Bayesian estimation is partially implemented in the `book/v0.1` branch and needs to be reviewed, completed and ported to `dev` branch. While not directly used in model selection, parameter estimation is needed once a structure is found.

#### Implement basic structure search strategies that optimize score

Each of the search strategies below will be implemented as a `StructureEstimator` (parametric on a data set and a score):

- Exhaustive search
- First-ascent hill climbing (HC)
    - Start at a given starting DAG
    - Sample operations from [“add edge”,”remove edge”,”reverse arrow”], evaluate score and modify DAG whenever score increases.
    - Converges to local maximum
- Greedy Equivalence Search (GES) (as described e.g. here)


## Milestone 3: Enhanced score-based structure learning

The following enhancements will be implemented to improve performance of both HC and GES.

#### Tabu lists
Tabu search forces the algorithm to explore new structures by preventing the reversal of recent structure changes, e.g. the last 100. [PGM09, page 816] says this already improves performance significantly.

#### Make sure score decomposability is used optimally
[PGM09, page 818f] suggest that search algorithms could directly operate with “delta scores”, that indicate whether or not a local change increases the overall score. Explore whether this improves performance over regular caching of the score method, using e.g. a memoization decorator.
Optional: Implement data perturbation (or random restarts) to escape local maxima
Data perturbation consists in small random manipulations of the underlying data set to escape local maxima without substantially changing the global structure. I would like to implement some simple mechanisms, as described in [PGM09, page 817].

## Milestone 4: Constraint-based structure learning
Add constraint-based structure learning as a new `StructureEstimator`:

#### Statistical independence tests on data sets

Implement method to perform statistical independence tests to query (conditional) independencies from data set. Method is internal to class and will, if possible, rely on e.g. `scipy.stats.chi2_contingency` rather than implementing the test by hand.

#### Constraint-based model construction

The PA algorithm [[LBN04](http://www.cs.technion.ac.il/~dang/books/Learning%20Bayesian%20Networks&#40;Neapolitan,%20Richard&#41;.pdf), page 550] constructs DAG patterns from faithful sets of independencies. Implement this algorithm with flexible “source” for independencies:
- A data set -> use independence tests
- A given set of faithful independencies -> directly work with them
- Any set of independencies -> for small models we can compute closure under semi-graphoid rules to obtain faithful set of independencies and continue from there.

## Milestone 5: MMHC algorithm

Implement the MMHC algorithm as a `StructureEstimator`. The algorithm is described step-by-step in  [[Tsamardinos et al](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.4729&rep=rep1&type=pdf), 2006], in three parts. It first uses a constraint-based model construction algorithm called MMPC that is faster than the PC procedure above, but only generates a DAG skeleton, i.e. an `UndirectedGraph`. Then, a modified hill climbing search with tabu list is used with a BDe score to orient the edges of the graph. This algorithm combines several of the previously implemented features.

## Milestone 6: Example gallery for structure learning tasks

Since pgmpy would benefit from some show cases, the final milestone is dedicated to creating some written content and applications.

#### Example gallery for website
Write some guiding introductory examples for structure learning using pgmpy, to illustrate the newly added features. _Target audience: new visitors to pgmpy._

#### Case studies for structure learning tasks
Implement & describe non-trivial show cases for structure learning, for example by replicating structure learning studies/papers in pgmpy. _Target audience: people interested in structure learning._

#### Performance tests
Extend [pgmpy-benchmarks](https://github.com/pgmpy/pgmpy-benchmarks) to include some performance statistics for the structure learning methods in pgmpy (and potentially other libraries). Performance tests are valuable information for anyone interested in real applications.

#### Structure learning tutorial for pgmy_notebook
Add structure learning tutorial in a new page for the “[pgmpy_notebook](https://github.com/pgmpy/pgmpy_notebook)”.
