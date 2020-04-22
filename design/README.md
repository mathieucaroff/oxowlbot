# Question bot design

- [Specification](#specification)
- [Requirement analysis](#requirement-analysis) (internal requirements, structure)
- [Approach](#approach)
- [Structure](#Structure)

# Specification

The bot can answer three kinds of questions:

- (QA) What-is-known-about questions:
  Who is <I>?
- (QB) Invidual-of-class questions:
  Who is a <C>?
- (QC) Relation questions:
  Who is <Relation> with <I>?

Syntaxical analysis is sufficient to distinguish (QC), however the distinction between (QA) and (QB) relies on lexical analysis.

This raises a question: what should be done when the syntax analysis matches for
both (QA) and (QB), but the lexical analysis also fails for both?

## Good handling of edge cases

The following situations are edge cases:

- (ECA) The bot finds no matching syntax. [Syntax failure]
- (ECB) The bot finds one or several matching syntaxes, but for each of them, the lexical analysis fails [Lexical failure]
- (ECC) The bot finds several matching syntaxes and several of them are lexical matches. [Form Ambiguity]
- (ECD) The bot finds one matching syntax with valid lexic, but meanings for a ter and several of them are lexical matches. [Lexic Ambiguity]

### ECA - Syntax failure

In case of a syntax failure, the bot should report the number of syntax tested,
and either propose the user with a way to obtain some help, or directly print
said help.

### ECB - Lexical failure

When the a lexical failure happens, the bot should be consistent in the way
it replies. It should list all the recipes for which syntax analysis was
successful, and conclude that lexical analysis failed for all of them:

```
Who is happy?

Your sentence matches 2 of the forms I know:
- Who is <I>?
- Who is <C>?
but the word you chose "happy" is unknown to me.
```

According to the word, it should conclude:

```
The word you chose "friend" is known as a [relation], but not as a [individual], nor as a [class].
```

### ECC - Form Ambiguity

When some ambiguity on the form occures, the bot should detect it and report it, before consistently picking one of the options. More specifically, the chosen option shall be the first matching case.

```
Your sentence completly matches the following forms:
- Who is <I>?
- Who is <C>?
I selected the first of them "[Who is <I>?]" and worked from there.
```

### EDD - Lexic Ambiguity

When some ambiguity on the form occures, the bot should detect it and report it, before consistently picking one of the options. More specifically, the chosen option shall be the first matching case.

```
The name "[word]" is lexically ambiguous. It designates the following individuals:
- [word A]
- [word B]
I selected the first of them "[word A]" and worked from there.
```

# Requirement analysis

Question bot will use the following separate features to be able to produce the
expected behaviour:

- Sentence decomposition (stanza and normalizeSentence)
- For each command the bot can interpret, it needs:
  - **Syntax analysis** of the normalized sentence, both match and extraction.
  - **Lexical analysis** of the key terms resulting from the syntax analysis, both match and translation. In case of success, lexical analysis can encounter lexical ambiguity, and thus require warning the user.
  - A definition of the **query** to perform against the OWL file
  - A **template** to produce the answer using the query results
- An algorithm which handles edge cases. These cases are mentioned and drafted
  in the [specification](#specification). After the fact note: the algorithm is actually very simple, consisting of two consecutive for loops.
- A correspondance table matching relation lemma identifiers to their OWL counterparts.

# Approach

## Sentence decomposition

It consists of running stanza on the sentence, and then fusing all the
resulting data in one string. The latter operation is what is called "sentence normalization".

### Syntax analysis

Syntax analysis uses regexes to retrieve an array of word ids from the normal sentence.

In simple cases, a single regex execution is sufficient to extract the ids. In more complicated cases, if there are repeated groups, the system will need a round to extract the repetition segment, and then process said segment to extract each repetition using a substitution with the /./g flag enabled.

### Lexical analysis

Lexical analysis can then use this array of ids along with the original stanza
result data to accept or refuse the match. In case it accepts it, the lexical
analysis needs to provide the translations of the key lexical terms to their
ontologic names.

The translation begins with the normalisation of the term. The depends on the nature identified for it by the syntax analysis:

- Relation names, class names and individual names are each matched against a table obtained at runtime. This includes aliases.
- In the case of individual names, this table associates each name to an array of one or several corresponding Owl names. When names are compound (e.g. "Twilight Sparkle") any subset of consecutive words from the name can be used to designate the individual. This may cause name ambiguity, hence the use of
  arrays of names to model it.
- In the case of relation names or a class name, for each OWL relation and each OWL name, the table associates the single designation name to their OWL name.

### Owl query

All owl operations rely on the `ontology` object.

### Answer formatting

The query result is interpolated in the template of the recipe, and the string
result is returned.

Answer templates:

- Who is Fluttershy?

```
Fluttershy is a Pegasus.
Fluttershy is friend with Twilight Sparkle, Discord, ...
Fluttershy is child of Posey Shy and Gentle Breeze.
```

- Who is a kirin?

```
There are [n][kirin]s:

- Automn Afternoon
- Automn Blaze
- Cider Glow
- ...
```

- Who is friend with Twilight Sparkle?

```
There are [n] creatures who are friend with Twilight Sparkle. They are:
- Moon Dancer
- Tempest Shadow
- Sunset Shimmer
```

# Structure

The decomposition of the app in communicating modules.
