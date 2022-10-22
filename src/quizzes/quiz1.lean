/-
CS2120 Fall 2022 Sullivan. Quiz #1. Edit your answers into
this file using VSCode. Save the file to your *local* hard 
drive (File > Save As > local > ...). Submit it to the Quiz1
assignment on Collab.
-/

/-
#1: For each of the following questions give a yes/no answer 
and then a very brief explanation why that answer is correct.
To explain why your answer is correct, name the specific rule
of inference that tells you it's correct, or explain that 
there is no such valid inference rule.
-/

/-
#1A

If a ball, b, is round *and* b is also red, is b red?

A: yes/no: yes

B: Why? By AND elimination right, X AND Y implies Y


#1B

If flowers make you happy and chocolates make you happy,
and I give you flowers *or* I give you chocolates, will
you be happy?

A: yes/no: yes

B: Why? By the rule of OR elimination


#1C: If giraffes are just zebras in disguise, then the 
moon is made of green cheese?

A. yes/: yes

B. Why? False implies false is true (not an inference rule but a rule of implication)


#1D. If x = y implies that 0 = 1, then is it true that
x ≠ y?

A. yes/no: yes

B. Why? If P implies false then it is equal to Not(P)



#1E. If every zebra has stripes and Zoe is a Zebra then
Zoe has stripes.

A. yes/no: yes

B. Why? rule of arrow elimination. Zebra implies stripes, Zoe is a Zebra, therefore stripes


#1F. If Z could be *any* Zebra and Z has stripes, then 
*every* Zebra has stripes.

A. Yes/no: yes

B: Why? The "for any" means Z is an arbitrary Zebra so yes all Zebras have stripes


#1G. If whenever the wind blows, the leaves move, and 
the leaves are moving, then the wind is blowing.

A. yes/no: no

B. Why? Fallacious: affirming the conclusion. False can imply true


#1H: If Gina is nice *or* Gina is tall, and Gina is nice,
then Gina is not tall. (The "or" here is understood to be
the or of predicate logic.)

A. yes/no: no

B. Why? Fallacious: Affirming the disjunct. Just because one side of the OR is true doesn't mean the other is false
-/



/- 
#2

Consider the following formula/proposition in propositional
logic: X ∨ ¬Y.

#2A: Is is satisfiable? If so, give a model (a binding of 
the variables to values that makes the expressions true).
X: True
Y: False

#2B: Is it valid? Explain your answer. 
No, if X is False and Y is true then the proposition would be false

-/


/-
#3: 

Express the following propositions in predicate logic, by
filling in the blank after the #check command.

If P and Q are arbitrary (any) propositions, then if (P is 
true if and only if Q is true) then if P is true then Q is 
true.
-/

#check ∀(P Q: Prop), P ↔ Q




/-
#4 Translate the following expressions into English.
The #check commands are just Lean commands and can
be ignored here. 
-/


-- A
#check ∀ (n m : ℕ), n < m → m - n > 0

/-
Answer: If n and m are any natural numbers, 
        if n is less than m
        then m - n > 0
-/

-- B

#check ∃ (n : ℕ), ∀ (m : nat), m >= n

/-
Answer: There is some natural number, n, that for all       natural numbers, m, 
m is greater than or equal to
-/


-- C

variables (isEven: ℕ → Prop) (isOdd: ℕ → Prop)
#check ∀ (n : ℕ), isEven n ∨ isOdd n

/-
Answer: For any natural number n,
n is even or n is odd
-/


-- D

#check ∀ (P : Prop), P ∨ ¬P

/-
Answer: For every proposition P, P is either true or false
-/


-- E

#check ∀ (P : Prop), ¬(P ∧ ¬P)

/-
Answer: For every proposition P, P cannot be both true and false
-/


/-
#5 Extra Credit

Next we define contagion as a proof of a slightly long
proposition. Everything before the comma introduces new
terms, which are then used after the comma to state the
main content of the proposition. 

Using the names we've given to the variables to infer
real-world meanings, state what the logic means in plain
natural English. Please don't just give a verbatim reading
of the formal logic. 
-/

variable contagion : 
  ∀ (Animal : Type) 
  (hasVirus : Animal → Prop) 
  (a1 a2 : Animal) 
  (hasVirus : Animal → Prop)
  (closeContact : Animal → Animal → Prop), 
  hasVirus a1 → closeContact a1 a2 → hasVirus a2


