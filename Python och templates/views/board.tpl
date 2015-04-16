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
			<a href="home">
			<img src="../Bilder/vitlogga.png" alt="Nabologga" style="width:260px;height:82px;border:0"></a>
		</div>
		<p id="user">
			<a href="myProfile">{{username}}</a>
		</p>
		<div id="loggaUt">
			<a href="index.html">Logga ut</a>
		</div>
	</header>

	<nav>
		<nav id="profile">
			<ul>
				<li><p id="user"><a href="myProfile">{{username}}</a></p></li>
				<li><a href="editProfile.html" class="nav">Redigera min profil</a></li>
			</ul>
		</nav>

		<nav id="board">
			<ul>
				<li><a href="board.html" class="nav">Anslagstavlan</a></li>
			</ul>
		</nav>

		<nav id="messages">
			<ul>
				<li><a href="inbox.html" class="nav">Mina meddelanden</a></li>
				<li><a href="write.html" class="nav">Skriv nytt meddelande</a></li>
			</ul>
		</nav>

		<nav id="nabos">
			<ul>
				<li><a href="nabos" class="nav">Nabos</a></li>
			</ul>
		</nav>
	</nav>

	<div id="content"
		<div id="bodySquare">
			<p>Board!
			</p>
		</div>
	</div>
	

	<footer>
		<a href="contact.html">Kontakta oss</a>
		<a href="about.html">Om Nabo</a>
		<a href="help.html">Hjälp</a>
	</footer>

	</div>
</html>