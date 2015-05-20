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
				<a href="/myProfile/">{{username}}   </a>
				<a href="/">  Logga ut</a>
				</p>
			</div>
		</header>

		<nav>
			<nav class="profile">
				<ul>
					<li><a href="/myProfile/" class="nav"> Min Profil </a></li>
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
				

				<p class="inboxMessages"><a href="/messageView/"><span style="font-weight:bold"> Lasse Löpare</span><br>05:30? Så har man det gjort :)
				</a></p>

				<p class="inboxMessages"><span style="font-weight:bold"> Martin Chard</span><br>Supersnällt att du matar katterna i helgen!
				</p>

				<p class="inboxMessages"><span style="font-weight:bold"> Hannes Dernbrant</span><br>Gårdsfest på lördag!
				</p>

				<p class="inboxMessages"><span style="font-weight:bold"> André Sjöroos</span><br>Tack för lånet av borrmaskinen!
				</p>

				<p class="inboxMessages"><span style="font-weight:bold"> Klara Hertzell</span><br>Jag är tyvärr i Sthlm då...
				</p>

				<p class="inboxMessages"><span style="font-weight:bold"> Malin Browall</span><br>Yes!
				</p>
			</div>
	

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>