title: Semantics for the Logical Connectives
date: 24.03.18


Model-theoretic semantics (as presented by Tarski) provides a formal account of the meaning of the logical vocabulary ($\land, \lor, \forall, \ldots$). In summary:

Given the usual language of first order logic $\mathcal L$, we first define the notion of a *model* $\mathfrak M_{\mathcal L}$. A model fixes the domain of individuals, and assigns an extension to the non-logical vocabulary of the language (=specifies what the variable, predicate and function symbols *refer* to). In other words, the model fixes the extension of the non-logical part of the language.

One can then specify the meaning of the logical vocabulary by stating their recursive *satisfaction conditions* (or *truth-in-a-model conditions* or simply *truth conditions*), for example

If $\mathfrak M_{\mathcal L}$ is a model, then 

$$  \mathfrak M_{\mathcal L} \models \varphi \land \psi \colon\!\iff \mathfrak M_{\mathcal L}\models \varphi and \mathfrak M_{\mathcal L}\models\psi $$

the *meaning* of $\varphi \land \psi$, i.e. the truth condition is thus a function that yields a truth value, given a model:

$$\mathfrak M_{\mathcal L} \mapsto \mathfrak M_{\mathcal L} \models \varphi and \mathfrak M_{\mathcal L}\models\psi$$

In this sense, Tarski's model theoretic semantics, is a semantic theory only of the logical vocabulary. It is not concerned with the meaning of the non-logical symbols. The connectives of first-order logic are *truth-functional* or *extensional*, that is, their truth conditions do not depend on the *meaning* (for sentences: truth conditions) of the non-logical constituents, but only on their extension (for sentences: truth value). Hence, it is sufficient that a model specifies the extension of the non-logical vocabulary to state the truth-conditions (meaning) of the 1st order connectives.

When extending the semantic theory to also account for the meaning of modalities such as *necessity*, one has to move to possible worlds semantics (Kripke models). Here, the semantic value assigned to a proposition by a Kripke model is no longer merely a truth value (extension) but a truth condition, i.e. a *subset of worlds where the proposition is true* (meaning, intension). This is so because modal vocabulary is *intensional* that is, it's meaning does not only depend on the extension of its argument (truth value) but on its meaning (truth-condition).

Further extension of this formal approch to semantics include: indexicals, .., .. and some require further refinement of the *semantic value* assigned to vocabulary, sentences of the language. It turns out, that only the meaning of the *logical connectives* of first order logic can be accounted for with a merely extensional model theory that only fixes the reference, but not the meaning of the non-logical. In fact, this is how Tarski defined what logical vocabulary is: that part of language, the meaning of which does not depend on the meaning, but merely the extension of its constituents.

Where does this leave *theories formulated in first order logic*?

Important such theories include (the first order axiomatisation of) Peano Arihmetic, and ZFC set theory. 
These theories involve certain non-logical symbols, such as $+,S,\in$, and come with a set of axioms that inform us about the behavior about those symbols. The axioms, however, fall short of specifying the meaning (truth conditions) of the new connectives. In fact, they even fall short of specifying the extension of the new connectives, and necessarily so. The theories, if, consistent have different models and each model assigns its own extension to e.g. the $\in$-predicate.

Model-theory of ZFC does not provide a semantic theory of set theory, when semantic theory is understood as providing a formal account of meaning. It is not concerned with the truth-conditions of the $\in$ predicate. A model of ZFC does not fix the meaning of $\in$, merely its extension. And the axiomatic theory does not fix a model, and thus only partially informs us about the extension of $\in$.

In summary, while Tarski's model theoretic definition of truth provides a semantic theory (truth conditions!) for the logical connectives, and, through certain extensions, for modal connectives and indexicals, etc., it does not account for the meaning of non-logical symbols. 

Model theory is not a semantic theory for any axiomatic theory built in the language of first order logic. The meaning of non-logical constituents of such a theory is syntactically described via the axioms. Nowadays, where "to give a semantics" just means to giva a basic model theory, one has to be careful to avoid confusion:

Model theory of ZFC is not a semantic theory of set theory, because the *'semantic' values* a model assigns are merely extensions not meanings. It does not attempt to fix truth-conditions of the sentences of set theory and it does not attempt to account for the meaning of $\in$. It is a syntactic theory of $\in$. Regarding set theory, the usual extension for assigning truth-conditions to atoms/sentences, namely the move to possible worlds semantics is possible without reinterpretation of that semantics, because the truths of set theory are considered *necessary*, which in that semantics means true at every world and this already fixes the semantic value such that all truths of set theory get assigned the same meaning, same for all falsehoods.

In particular, ZFC and its model theory is not a formal account of the semantics of mathematics. 

When using the notion of a "standard model of set theory", that supposedly fixes the meaning of membership, this is not very satisfactory: Mathematical meaning, with mathematical theorems being necessary, shouldn't vary with models. Next it only fixes extension, and lastly an undefined notion of standard model is murky and subjective. How do i know my standard model is the same as that of others?









####ToMaybe:
* Theory of meaning vs theory of reference
* Tarski semantics is theory of meaning for propositional/1st order connectives
* ... but merely theory of reference for axiomatic theories formulated in it (models only fix extension of the non-logical symbols)? Because not concerened with meaning (truth-conditions) of the non-logical.
* A formal account of meaning based on extensional theory is too limited for all but logic; some things (modalities, ...) can be given truth-conditions in a possible worlds semantics.


