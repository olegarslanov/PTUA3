# Kad pasidalinti failai revizijai su kolega

# 1. Web browser github.com sukuriu repository -> new, suteikiu pavadinima: <repozitorijos pavadinimas>
# 2. Atidarau Git Bash:
# a) nukeliauju i direktorija kurioje randasi revizuojami failai
# b) ivedu : git clone <http adresas>    (nukopijuoju revizuojamu failu <http adresas> is github.com)
# c) ivedu : <kodo tekstas>    (kopijuoti teksta is pastraipos: "…or create a new repository on the command line")
# d) ivedu : git checkout -b <sakos pavadinimas> (cia sukuriu brancho nauja saka)
# e) ivedu : code . (atsidarys VS code programa)
# 3. Atidarau VS code:
# a) atidarau folder su revizuojamais failais
# b) ivedu : git add .
# c) ivedu : git commit -m "2023_05_16"
# d) ivedu : git push
# 4. Nauja projekto atsaka sukurta
# 5. Web browser github.com ieinu i repozitoriju spaudziu "Settings"-> "Collaborators" -> "Add people" ... dadedu kas gales koreguoti repozitoriju
# 6. spaudziu: pull request ir


# Kad sukurti nauja branch reikia 'Terminalo' lange ivesti:
# "git checkout -b <branch_name>"


# Kad pereiti is pagrindinio branch i pagalbini ivedam:
# "git checkout <branch_name>"


# Norint padaryti merge reikia ivesti is vieno branch i kita:
# "git merge <branch_name>"


# Kad paziureti kiek yra branch ivesti:
# "git branch"


# Kad persiusti i github pakeitimus:
# "git add ." - paruosiau visus pakeitimus is branch
# "git commit -m <'komentaras'>" - pridedu komentara kas per pakeitimai
# "git status" - pateikia info kas bus keiciama serverio atmintyje
# "git push" - perkeliu visus pakeitimus i github serveri


# Kad atsiusti is github pakeitimus i kompa:
# "git status" - pateikia info kas bus atsiusta
# "git pull" - atsiunciu visus pakeitimus i mano kompa


# Kad klonuoti failus is github i local reikia:
# github.com kopijuoju "Code" nuoroda
# tada atidarau terminale (ar git bash) direktorija, kurioje noriu kad butu klonuoti failai
# terminalo eiluteje irasau "git clone <nuoroda is github>"


# Kad isnaikinti branch reikia:
# "git branch -delete <branch name>" - naikinu is local
# "git branch -delete <branch name> -a" - naikinu branch ir is github serverio


# Papildomos komandos:
# "mkdir <folder name>" - sukurti nauja byla
# "ls" - galiu perziureti kokie failai yra direktorijoje
# ":q" - spaudziu kad iseiti is git log
# "code . " - paleisti programa Visual Stiudio Code
# "git log" -
