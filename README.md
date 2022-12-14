<div align="center">

# [πππ νμ±μ€κ² πππ](http://sparta-mark.shop/)

## π Intro π€

<b>νμ±μ€κ²</b>λ  μ€κ³  μ± κ±°λ μλΉμ€μλλ€. π

π [λ μμλ³΄κΈ°](https://github.com/innovation-camp/heonchaegjulge/wiki) π

## π¨ WireFrame π

![Screen Shot 2022-08-04 at 12 25 36 PM](https://user-images.githubusercontent.com/60090391/182756494-25a64a89-af5d-46d5-8e68-ed7454e34847.png)

## π©π»βπ» Contributors π§π»βπ»

| [μ€μμ§](https://github.com/blingblin-g) | [κΉμ μ](https://github.com/Dajeong09) | [λ°μΈμ](https://github.com/marksenee) | [μ΄λ€μ ](https://github.com/Dajeong09) | [μ₯νμ±](https://github.com/Artlogy) |
|---------------------------------------|---------------------------------|-------------------------------------|--------------------------|-----------------------------------|
| λ‘κ·ΈμΈ / λ‘κ·Έμμ                            | λ‘κ·ΈμΈ / λ‘κ·Έμμ                      | κ²μκΈ CRUD                            | κ²μκΈ CRUD                 | κ²μκΈ λͺ©λ‘<br/> / μ°μ»΄νμ΄μ§               |
|              Back-end                 |             Front-end                    |        Front-end                             |             Back-end             | Front-end                         |

## βοΈ Tech Stack π 
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Python-blue?style=flat-square&logo=python&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Flask-gray?style=flat-square&logo=flask&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/MongoDB-darkgreen?style=flat-square&logo=mongodb&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/Jinja2-red?style=flat-square&logo=jinja&logoColor=white"/>
<img style="margin:5px; border: 2px solid white; border-radius: 20px" src="https://img.shields.io/badge/AWS-232f3e?style=flat-square&logo=amazon&logoColor=white"/>

</div>

## πΌ How to run βΈ

### Python version
```shell
$ python -V
  Python 3.8.9
```

### clone repository
```shell
$ git clone https://github.com/innovation-camp/heonchaegjulge.git
```

### into the repository
```shell
$ cd heonchaegjulge
```

### install packages
```shell
$ pip install -r requirements.txt
```

### start app
```shell
$ flask run
```

## π Directory Structure π

```shell
π¦ app
 β£ π controller
 β£ π decorators
 β£ π middleware
 β£ π static
 β β£ π css
 β β£ π image
 β β£ π js
 β£ π templates
 β β£ π account
 β β£ π components
 β β£ π error
 β β£ π post
 β£ π __init__.py
 β£ π constants.py
 β£ π db.py
 β π utils.py
```

## πΎ Database Schema πΏ

### User

```python
    {
        _id: <ObjectId>,
        nickname: "haha",
        email: "abc@gmail.com",
        password: "sljriowqejfj3weo;'qfijewoj124j!" # hashing
        created_at: DATETIME
    }
```

### Post

```python
{
	_id: <ObjectId>
	title:
	description:
	created_at:
	updated_at:
	is_selling:
	condition:
	price:
	writer: {
                    id: , 
                    nickname:
                }
	is_soldout:
	location:
	genre:
	contact:
}
```
