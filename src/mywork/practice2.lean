import data.set

def isEven (n : ℕ) : Prop := n%2 = 0
--Set comprehension notation
--all natural numbers n such that n is even
def evens : set ℕ := { n : ℕ | isEven n }

#check evens
#check isEven

#reduce isEven
#reduce evens

#reduce evens 4 --true so in evens set
#reduce evens 5 --not true so not in evens set


def strings5 := {s : string | s.length = 5}

#reduce strings5 "test"
#reduce strings5 "world"

example : strings5 "Lean!" :=
begin
unfold strings5,
show "Lean!".length = 5,
apply rfl
end

-- example : strings5 "yup" :=
-- begin
-- unfold strings5,
-- show "yup".length = 5,
-- apply rfl
-- end

example : ¬strings5 "yup" :=
begin
assume h,
unfold strings5 at h,
cases h,
end

--set membership
example : "world" ∈ strings5 :=
begin
unfold strings5,
show {s : string | s.length = 5} "world",
show "world".length = 5,
show (5 = 5),
apply rfl,
end

example : "world" ∈ strings5 :=
begin
exact rfl,
end

example : "yup" ∉ strings5 :=
begin
show ¬(strings5 "yup"),
assume h,
unfold strings5 at h,
cases h,
end

def set135 := {n : ℕ  | n = 1 ∨ n = 3 ∨ n = 5}:
#reduce set135 5

example : 5 ∈ set135 :=
begin
right,
right,
exact rfl,
end

example : 4 ∉ set135 :=
begin
assume h,
cases h,
cases h,
cases h,
  cases h,
  cases h,
end

example : 4 ∉ set135 :=
begin
assume h,
repeat {cases h},
end

def my_empty_set (T : Type) := {t : T | false}


#reduce (∅ : set nat)