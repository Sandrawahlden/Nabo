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
				<p class="user">
				<a href="/myProfile/">{{username}}   </a>
				<a href="/">  Logga ut</a>
				</p>
			</div>
		</header>

		<nav>
			<nav class="profileClick">
				<ul>
					<li><p class="user"><a href="/myProfile/"> Min Profil </a></p></li>
					<li><a href="/editProfile/" class="nav">Redigera min profil</a></li>
				</ul>
			</nav>

			<nav class="board">
				<ul>
					<li><a href="/home/" class="nav">Anslagstavlan</a></li>
				</ul>
			</nav>

			<nav class="messages">
				<ul>
					<li><a href="/inbox/" class="nav">Mina meddelanden</a></li>
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
			<div id="editProfile">
				<p id="editProfileText">REDIGERA MIN PROFIL</p>

				<form action="/editProfile/" method="POST" class="form">
					<p class ="profile_pic">URL till profilbild</p>
					<input type="text" name="profile_pic" id="EDprofile_pic" value="{{pic}}">	
		
					<p class ="name">Förnamn</p>
					<input required type="text" name="name" id="EDname" value="{{firstname}}">	
						
					<p class="surname">Efternamn</p>
					<input required type="text" name="surname" id="EDsurname" value="{{lastname}}">	
						
					<p class="age">Ålder</p>
					<input type="text" name="age" id="EDage" value="{{age_1}}">

					<p class="lgh">Våning</p>
					<input  type="text" name="lgh" id="EDlgh" value="{{appartment}}">			
						
					<p class="email">E-postadress</p>
					<input required type="email" name="email" id="EDemail" value="{{mail}}">			
				
					<p class="tel">Telefonnummer</p>
					<input type="text" name="tel_nr" id="EDtel_nr" value="{{tel}}">			
			
					<p class="likes">Om mig</p>
					<input type="text" name="likes" id="EDlikes" value="{{like}}">			
		
					<p class="password">Byt lösenord</p>
					<input type="password" name="pwd_1" class="EDpassword" placeholder="Nytt lösenord:">	
						
					<p class="password">
					<input type="password" name="pwd_2" class="EDpassword" placeholder="Bekräfta nytt lösenord:">	
						
					<p id="acceptChange">Bekräfta ändringar genom att ange ditt nuvarande lösenord</p>
								
					<input type="password" required name="old_pwd" class="EDpassword" placeholder="Skriv ditt gamla lösenord:">	
									
					<input name="update" type="submit" value="Uppdatera" id="EDsubmit">
				</form>
			</div>

			<div id="moving">
				<button id="move" type="button">Jag har flyttat!</button>
			</div>
		</div>
		

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>