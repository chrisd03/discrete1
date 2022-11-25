--if theres someone everyone loves, then everyone loves someone
example
  (Person : Type)
  (Loves : Person → Person → Prop)
  :
  (∃ (p : Person), ∀(q : Person), Loves q p) → (∀ (p : Person), ∃ (q : Person), Loves p q)
  :=
begin
  assume h, --for the arrow
  cases h with lenny all_love_lenny, --exists.elim → lenny and proof everyone <3
  assume bruce, -- forall intro
  apply exists.intro lenny _, --show there's someone bruce loves
  exact all_love_lenny bruce, --we know everyone loves lenny already so apply
end

def exists_elim := 
  ∀ {X : Type}              -- for any type, X 
    {P : X → Prop}          -- for any predicate on values of this type
    {Y : Prop},             -- for any "concluding" proposition, Y
    (∃ (x : X), P x) →      -- if we're given a proof that there's an x satisfying P
    (∀ (x : X), P x → Y) →  -- then if for every x that satisfies P Y is true
    Y   

example : exists_elim :=
begin
  unfold exists_elim,
  assume x P,
  assume Y,
  assume exists_x_with_P,
  assume if_any_x_has_P_then_Y,
  cases exists_x_with_P with w Pw,
  exact if_any_x_has_P_then_Y w Pw,
end

--identity of natural numbers
def id_nat : ℕ → ℕ
| n := n

--generic identity : something returns itself
def id_T : ∀ (T : Type), T → T
| T t := t

#eval id_T nat 5
#eval id_T bool tt
#eval id_T string "hey"

--same but doesn't require type as parameter
def id_T' {T : Type} : T → T
| t := t

#eval id_T' 5
#eval id_T' tt
#eval id_T' "hey"

#check @id_T'
