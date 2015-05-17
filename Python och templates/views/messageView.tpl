<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>


	<div id="wrapper">

		<header>
			<div id="logga">
				<a href="/home/">
				<img src="/static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0"></a>
			</div>
			<div id="loggaUt">
				<p id="adress"> Rönnblomsgatan 11</p>
				<p id="user">
				<a href="/myProfile/">{{username}}</a>
				<a href="/">Logga ut</a>
			</div>
		</header>

				<nav>
			<nav class="profile">
				<ul>
					<li><p id="user"><a href="/myProfile/">{{username}}</a></p></li>
					<li><a href="/editProfile/" class="nav">Redigera min profil</a></li>
				</ul>
			</nav>

			<nav class="board">
				<ul>
					<li><a href="/home/" class="nav">Anslagstavlan</a></li>
				</ul>
			</nav>

			<nav class="messagesClick">
				<ul>
					<li><a href="/inbox/" class="nav"><span style="color: #4d6630">Mina meddelanden</span></a></li>
					<li><a href="/write/" class="nav">Skriv nytt meddelande</a></li>
				</ul>
			</nav>

			<nav class="nabos">
				<ul>
					<li><a href="/nabos/" class="nav">Nabos</a></li>
				</ul>
			</nav>
		</nav>

		<div id="content">
				<p class="from">Hej! Jag bor precis ovanför dig. Har sett att du ofta är ute och springer på morgonen. Jag springer ultralopp. Säg till om du vill spriga tillsammans någon gång :)
				</p>

				<p class="me">Tja tja, det låter ju supernice. Jag har precis gjort min första mara. Hade varit schysst med sällskap på distanspassen. 
				</p>

				<p class="from">Grattis! Hoppas loppet gick bra. Jag brukar ha ett distanspass på söndagar. Ca 35 km. Sugen?
				</p>

				<p class="me">Fett. Tid?
				</p>

				<p class="from">05:30? Så har man det gjort :)
				</p>

				<p id="fakeWrite">Svara</p>

				<p id="fakeSend">Skicka</p>
		</div>
	

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>
	</div>
</html>