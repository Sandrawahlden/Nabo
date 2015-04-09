<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>

	<header>
		<p>Nabologga här</p>
		<p id="user">
			%for i in username:
				<a href="/user/{{i}}">{{name}}</a>
			%end
		</p>
		<p>
			<a href="board">Logga ut</a>
		</p>
	</header>

	<body>
		<nav id="profile">
			<ul>
				<li><a href="myProfile.html" class="nav">Min profil</a>
				<li><a href="editProfile.html" class="nav">Redigera min profil</a>
			</ul>
		</nav>

		<nav id="board">
			<ul>
				<li><a href="board.html" class="nav">Anslagstavlan</a>
			</ul>
		</nav>

		<nav id="messages">
			<ul>
				<li><a href="inbox.html" class="nav">Mina meddelanden</a>
				<li><a href="write.html" class="nav">Skriv nytt meddelande</a>
			</ul>
		</nav>

		<nav id="nabos">
			<ul>
				<li><a href="nabos.html" class="nav">Nabos</a>
			</ul>
		</nav>

	</body>

	<footer>
		<a href="contact.html">Kontakta oss</a>
		<a href="about.html">Om Nabo</a>
		<a href="help.html">Hjälp</a>
	</footer>
</html>









