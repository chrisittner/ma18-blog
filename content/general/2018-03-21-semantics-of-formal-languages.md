title: Semantics of formal languages
date: 20.03.2018

The first step when introducing a formal language is to define its alphabet & grammar (syntax). 
Which symbols are part of the language? 
How are the words and sentences (aka formulas, expressions) of the language formed?
Next, one has to explain *how the language is to be understood*. 
*What do the words and sentences mean?* 
 How should we interpret them?
The study of meaning is *semantics*. 

The approach to semantics used in my thesis, *(Logical) Inferentialism* (also called *proof-theoretic semantics*), is a non-standard account of meaning for formal languages. It makes sense to first recall the received approach, for pointing out essential differences. The standard approach to semantics in logic is to identify the meaning of a sentence with its *truth conditions*, thereby reducing sentence-meaning to the notion of truth. Following Tarski, truth is analyzed as *truth in a model*.
This received approach is so ubiquitous nowadays, that 'to give a semantics' usually just means to give a basic model theory for the language in question.

We briefly outline the usual semantics for formal logic and point out basic features of this account.
We then compare and contrast this to the operational understanding of the formal languages used for computer programming.



### *Truth-conditional* semantics for sentences:

* Tarski semantics: Give *Model*, map words to objects ("meanings", "semantic values"). Sentences are mapped to values *true* or *false* by a model (satisfaction relation). **Extensional meaning** = denotation = truth value

* Kripke semantics: Give set of models, each maps words to objects. Sentences are mapped to subsets of set of models (those in which they are satisfied (=true)). **Intensional meaning** = sense_Fr?  = truth conditions

* Sentence-meaning explained in terms of truth. Understand what a sentence means = be aware of the conditions for its truth.

### *Operational* semantics?

*operational* (CS) vs *denotational* (Logic) semantics.