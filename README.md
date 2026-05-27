# Download mit repository
```bash
git clone https://github.com/Malik-sundxtech/AnvProg
```
Husk du skal have et activt venv for at køde koden

Se et godt eksempel på et flowchart og klassediagrammer i [her](Workshops/Workshop_2/Delopg1_workflow.md)


# Noter til mig selv
På min windows computer skal jeg for at køre jupyter notebook brugefølgende kommando:
```bash
python -m notebook
```

**Flowchart notation:** \
Cirkler = start/stop \
Rektangler = handling \
Romber = beslutninger(ja/nej)

**Class Diagram notation:** \
"+" = public \
"-" = private \
"#" = protected 


```mermaid
flowchart LR

1[OOP] --> 2[Signal behandling] --> 3[Population data]

```
```mermaid
flowchart TD

1[OOP] --> 1.1[OOP 1] --> 1.2[OOP 2] --> 1.3[OOP 3] --> 1.4[OOP workshop]

2[Signal behandling] --> 2.1[Signal behandling 1] --> 2.2[Signal behandling 2] --> 2.3[Signal behandling 3] --> 2.4[Signal behandling workshop]

3[Population data] --> 3.1[Population data 1] --> 3.2[Population data 2] --> 3.3[Population data 3] --> 3.4[Population data workshop]
```