<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="../static/style.css">
		<script type="text/javascript" src="/static/JS/Password check.js"></script>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>

	<body>
	
	<div id="mamaWrapper">
		<div id="indexWrapper">
			<div id="logga">
				<a href="/">
					<img src="../static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:250px;height:82px;border:0" >
				</a>
			</div>
		
		
			
				<div id="signin">
					<p class="indexPageText">LOGGA IN</p>

					<form action="/" method="POST" class="form">
					
						<p>
							<input required type="email" name="mail" id="emailSI" placeholder="Email">
						</p>			
						
						<p>
							<input required type="password" name="pwd" id="passwordSI" placeholder="Lösenord">	
						</p>
				
						<p class="submit">
							<input name="sign_in" type="submit" value="Logga in" class="button1">
						</p>
					</form>
				</div>

				<div id="welcomeText">
					<h1>Välkommen till Nabo!</h1>
					<p id="welcomeTextFirstPage">Nabo hjälper dig att identifiera och interagera med grannarna i din trappuppgång. Låna en hammare, ordna kattvakt eller bjud in till gårdsfest.</p>
				</div>
			</div>
			
			<div id="secondIndexWrapper">
				<div id="signUp">
					<p class="indexPageText">SKAPA ANVÄNDARE</p>	
						<form action="/myProfile/" method="POST" class="form">
						
							
								<input required type="text" name="name" id="nameLI" placeholder="Förnamn">	
							
								<input required type="text" name="surname" id="surnameLI" placeholder="Efternamn">	
							
							
							
								<input required type="email" name="email" id="emailLI" placeholder="Email">			
					

						
								<input type="password" required name="pwd_1" class="passwordLI" placeholder="Lösenord">	
							
								<input type="password" required name="pwd_2" class="passwordLI" placeholder="Bekräfta lösenord">	
							

						
								<input required type="text" name="adress" id="addressLI" placeholder="Gatuadress">	
							

							
								<input required type="text" name="city" id="cityLI" placeholder="Postort">	
						
							
							
								<input name="register" class="button1" type="submit" value="Registrera">
							
						</form>
				</div>
			</div>
		</div>
	</body>	
</html>


