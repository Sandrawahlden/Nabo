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
				<p id="user">
				<a href="/myProfile/">{{username}}</a>
				<a href="/">Logga ut</a>
			</div>
		</header>

		<nav>
			<nav id="profile">
				<ul>
					<li><p id="user"><a href="/myProfile/">{{username}}</a></p></li>
					<li><a href="/editProfile/" class="nav">Redigera min profil</a></li>
				</ul>
			</nav>

			<nav id="board">
				<ul>
					<li><a href="/home/" class="nav">Anslagstavlan</a></li>
				</ul>
			</nav>

			<nav id="messages">
				<ul>
					<li><a href="/inbox/" class="nav">Mina meddelanden</a></li>
					<li><a href="/write/" class="nav">Skriv nytt meddelande</a></li>
				</ul>
			</nav>

			<nav id="nabos">
				<ul>
					<li><a href="/nabos/" class="nav">Nabos</a></li>
				</ul>
			</nav>
		</nav>

		<div id="content"
			<div id="bodySquare">
				<div id="editProfile">
					<p id="editProfileText">Redigera Profil</p>	
<<<<<<< HEAD
					<button id="move" type="button">Jag har flyttat!</button>
						<form action="/editProfile/" method="POST" class="form">
						
							<p class ="profile_pic">URL till profilbild: </p>
								<input type="text" name="profile_pic" id="profile_pic" value="{{pic}}">	
							
							<p> Förnamn: </p>
							<p class ="name">
								<input required type="text" name="name" id="name" value="{{firstname}}">	
							</p>
								
							<p> Efternamn: </p>
							<p class="surname">
								<input required type="text" name="surname" id="surname" value="{{lastname}}">	
							</p>
							
							<p> Ålder: </p>
							<p class="age">
								<input type="text" name="age" id="age" value="{{age_1}}">
							</p>
							
							<p> Våning: </p>
							<p class="lgh">
								<input  type="text" name="lgh" id="lgh" value="{{appartment}}">			
							</p>
							
							<p> Email: </p>
							<p class="email">
								<input required type="email" name="email" id="email" value="{{mail}}">			
							</p>
							
							<p> Telnr: </p>
							<p class="tel">
								<input type="text" name="tel_nr" id="tel_nr" value="{{tel}}">			
							</p>
							
							<p> Om mig: </p>
							<p class="likes">
=======
						<form action="/editProfile/" method="POST" class="form">
						
							<p class ="profile_pic">URL till profilbild:
								<input type="text" name="profile_pic" id="profile_pic" value="{{pic}}">	
							</p>
							
							<p class ="name">Förnamn:
								<input required type="text" name="name" id="name" value="{{firstname}}">	
							</p>
								
							<p class="surname">Efternamn:
								<input required type="text" name="surname" id="surname" value="{{lastname}}">	
							</p>
							
							<p class="age">Ålder:
								<input type="text" name="age" id="age" value="{{age_1}}">
							</p>
							
							
							<p class="lgh">Våning:
								<input  type="text" name="lgh" id="lgh" value="{{appartment}}">			
							</p>
							
							<p class="email">Email:
								<input required type="email" name="email" id="email" value="{{mail}}">			
							</p>
							
							<p class="tel">Telnr:
								<input type="text" name="tel_nr" id="tel_nr" value="{{tel}}">			
							</p>
							
							<p class="likes">Om mig:
>>>>>>> a609dc596cf2dc5c68080b4bca8b60b0ba7f2ddf
								<input type="text" name="likes" id="likes" value="{{like}}">			
							</p>
							
							<p>Byta lösenord</p>
							<p class="password">
								<input type="password" name="pwd_1" id="password" placeholder="Nytt lösenord:">	
							</p>

							<p class="password">
								<input type="password" name="pwd_2" id="password" placeholder="Bekräfta nytt lösenord:">	
							</p>
							
							<div id="acceptChange">
								<p>Bekräfta ändringar genom att ange ditt lösenord</p>
								
								<p class="password">Gammalt lösenord:
									<input type="password" required name="old_pwd" id="password" placeholder="Skriv ditt gamla lösenord:">	
								</p>
							
								<p class="submit">
									<input name="update" type="submit" value="Uppdatera">
								</p>
							</div>
						</form>
				</div>	
			</div>
		</div>
		

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>