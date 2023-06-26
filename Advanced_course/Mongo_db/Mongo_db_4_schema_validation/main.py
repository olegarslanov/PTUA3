# BSON (Binary JSON) yra duomenų formatas, kuris naudojamas dokumentų saugojimui ir mainams MongoDB duomenų bazėje.
#  BSON turi savo tipo formatus, kurie nurodo, kaip skirtingi duomenų tipai turi būti reprezentuojami BSON formatu.
# Kai kurie iš populiariausių BSON tipo formatų yra:

# double - skaičius dviejų slankiojo kablelio formatu.
# string - tekstinė eilutė.
# object - BSON dokumentas, kuris yra raktas-vertės porų kolekcija.
# array - BSON masyvas, kuris yra reikšmių sąrašas.
# bool - loginė reikšmė true arba false.
# null - speciali reikšmė, nurodanti tuščią arba neegzistuojančią reikšmę.
# date - datos ir laiko reikšmė.
# int - sveikasis skaičius.
# long - ilgojo sveikojo skaičiaus formatas.
# decimal - skaičius su fiksuotu kiekiu skaitmenų po kablelio.
# timestamp - laiko žymė, naudojama BSON dokumentų pakeitimų seka.
# binary - binarinis duomenų srautas.
# regex - reguliarusis išraiškos objektas.
# javascript - JavaScript kodo eilutė.
# symbol - simbolio reikšmė.
# Tai tik keletas BSON tipo formatų pavyzdžių. Kiekvienas BSON tipo formatas turi savo taisykles ir savybes, kuriomis jis yra apibrėžtas.


# Validator: Валидатор определяет правила, которым должны соответствовать документы. Он указывается как словарь внутри validation_rulesсловаря.

# $jsonSchema: Ключ $jsonSchema указывает синтаксис схемы JSON для определения правил проверки. Он содержит основную часть правил проверки.

# bsonType: bsonTypeКлюч указывает ожидаемый тип данных для поля. Для него могут быть установлены такие значения, как строка, int, двойное число, массив, объект и т. д.

# required: Обязательный ключ указывает массив имен полей, которые должны присутствовать в документе.

# properties: Ключ свойств определяет проверку отдельных полей в документе. Каждое поле указывается в виде пары ключ-значение, где ключ — это имя поля, а значение — правило проверки для этого поля.

# Additional Validation Rules: в ключе свойств вы можете определить дополнительные правила проверки для каждого поля. Например, минимум и максимум можно использовать для указания диапазона значений
# числового поля, а шаблон можно использовать для принудительного применения определенного формата с помощью регулярных выражений.


# Pateiktas validation_rules yra žodynų (dictionary) objektas, kuris apibrėžia MongoDB validator taisykles. Šios taisyklės nustato reikalavimus dokumentams, kurie bus įterpti į MongoDB duomenų bazę.


# Šis konkretus validation_rules objektas nustato, kad dokumentas turi turėti tris privalomus laukus: 'name', 'age' ir 'email'. Kiekvienas iš šių laukų turi savo duomenų tipą ir galimus papildomus taisykles.

# 'name' turi būti teksto tipo (string) laukas.
# 'age' turi būti sveikųjų skaičių tipo (integer) laukas, kuris turi būti ne mažesnis nei 0.
# 'email' turi būti teksto tipo (string) laukas, kuris atitinka tam tikrą šabloną, aprašytą reguliariuoju išraiška ('pattern').
# Šie taisyklių nustatymai užtikrina, kad į MongoDB duomenų bazę bus įterpiami tik dokumentai, kurie atitinka šiuos reikalavimus.


# Define the validation rules as a dictionary
validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "age", "contact"],
            "properties": {
                "name": {"bsonType": "string"},
                "age": {"bsonType": "int", "minimum": 0},
                "contact": {
                    "bsonType": "object",
                    "required": ["email", "phone"],
                    "properties": {
                        "email": {"bsonType": "string"},
                        "phone": {"bsonType": "string", "pattern": "^[0-9]{10}$"},
                    },
                },
            },
        }
    }
}


# json object

shustras = {
    "name": "Antanas",
    "age": 20,
    "contact": {
        "email": "antanas@mail.lt",
        "phone": "0037065645823",
    },
}
