# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vendedora")
define e = Character("Eu")
define s = Character("Sistema Barato e Fajuto")
define l = Character("Locutor")
define h = Character(" ")
define c = Character("Clara")
define m = Character("Moça aleatória")
define r = Character("Rapaz estranho")
define d = Character("???")



image trem = "images/tremfora.jpg"
image fest = "images/festival.png"
image dormindo = "images/dormindo.png"
image patonotucupi = "images/patonotucupi.png"
image mandiocafrita = "images/mandiocafrita.jpg"
image fundopreto = "images/fundopreto.png"
image rapaz = "images/rapaz.png"
image tremfim = "images/tremfim.jpg"
image celular = "images/celular.jpg"
image banco = "images/banco.jpg"
image sistema = "images/sistema.png"
image clara = "images/clara.png"


# The game starts here.

label start:
    play music "audio/trem.mp3"

    scene dormindo
    show dormindo at truecenter:
        zoom 1
    with dissolve


    h "É dia e você está sentado no trem quase pegando no sono."
    v "Olha a mandioca, a mandioca!"
    h "A vendedora esbarra em você e você quase cai."
    h "Ela sai andando como se nada tivesse acontecido, deixando-o resmungando."
    e "Fala sér..."
    h "Você se ajeita na mochila e apoia a cabeça nela para voltar a dormir."

    stop music

    queue music "audio/tremfreio.mp3" noloop
    
    h "Trem freia bruscamente."
    e "Ah, qualé mano, me deixa dormir!"
    d "Bem vindo ao “É tudo mandioca”, onde eu, o sistema barato e fajuto te recebo."
    e "(resmunga)"
    s "Você não me deixa opção... Vou ser legal e te dar uma escolha:"

    menu:
        "Continuar dormindo":
            s "Que você tenha sorte nessa viagem."

            play music "audio/trem.mp3"
            
            h "Trem volta a andar nos trilhos."
            h "Você suspira por continuar finalmente a sua viagem e não ter que lidar com pessoas estranhas lhe incomodando."
            l "Próxima estação Macaxeira. Próxima estação Macaxeira."
            l "Por favor, passageiros desçam na próxima estação."
            l "Esse trem estará fora de serviço."
            l "Por favor, desçam na próxima estação Macaxeira." 
            h "Acorda e olha ao redor."
            e "Que raios de estação é essa. Não existe estação com esse nome em São Paulo."
            jump estacao

        "Levantar e descobrir quem está te incomodando":
            s "Oh vejo que você é muito inteligente."
            e "(Suspira)"

            scene sistema
            show sistema at truecenter:
            with dissolve

            s "Bem vejamos."
            s "Você precisa tomar cuidado na próxima estação porque tudo o que você encontrar ali pode ser venenoso e todo mundo, todo mundo mesmo vai tentar fazer você comer o que não é pra comer."
            e "É só eu chamar a polícia!"
            e "(Pega o celular do bolso)"
            e "Quem em sã consciência envenenaria alguém ainda na luz do dia e do jeito que você está falando."
            s "Você olhou o seu celular?"

            scene celular
            show celular at truecenter:
                zoom 0.7
            with dissolve

            e "(olha para a tela. Aparece sem sinal e o celular desliga logo em seguida. Ele tenta ligar sem sucesso.)"
            e "Mas o que??"
           
            scene sistema
            show sistema at truecenter:
            with dissolve

            s "Eu não disse?"
            s "Ah pera eu não disse."
            s "Estamos no mundo da mandioca."
            s "Mas não qualquer uma..."
            s "Estamos no mundo da mandioca brava de “É tudo mandioca”."
            e "(Se levanta e olha para a janela)"

            scene banco
            show banco at truecenter:
                zoom 0.7
            with dissolve
            
            s "Você não vai poder sair daqui até encontrar a única mandioca boa e comê-la."
            e "Mas que raio de mundo é esse?"
            s "Que você tenha sorte nessa viagem."
            s "(Desaparece no ar)"
            h "O trem volta a andar nos trilhos."

            play music "audio/trem.mp3"

            l "Próxima estação Macaxeira. Próxima estação Macaxeira."
            l "Por favor, passageiros desçam na próxima estação."
            l "Esse trem estará fora de serviço."
            l "Por favor, desçam na próxima estação Macaxeira." 
            e "Que raios de estação é essa. Definitivamente não existe estação com esse nome em São Paulo."
            stop music
            jump estacao

label estacao:
    scene fest
    show fest at truecenter:
        zoom 1
    with dissolve

    h "As portas se abrem."

    stop music

    play music "audio/festival.mp3"

    h "Tem várias barracas a sua frente e muitas pessoas conversando animadamente."      
    m "Olha mais um chegou para aproveitar nossos quitutes!"
    scene clara
    show clara at truecenter:
    with dissolve
    m "Pena que nenhum fica por muito tempo..."
    m "(Suspira)"
    c "Eu sou a Clara e quero te apresentar os melhores pratos feitos com mandioca."
    c "Gostaria de provar um?"
    
    menu:
             "Isso é pato no Tucupi? O que é isso, nunca ouvi falar.":
                scene patonotucupi
                show patonotucupi at truecenter:
                    zoom 1
                with dissolve

                c "É um prato delicioso. Sempre que posso eu como é um dos meus favoritos."
                e "(Pego um pedaço e como devagar, estranhando no início mas gostando no final.)"
                e "É realmente muito gostoso!"
                e "(Mordo mais um pedaço grande)"
                h "Clara vai embora e você começa a andar por entre as barracas olhando as comidas, despreocupado."
                h "A comida é tão gostosa e bem preparada."
                e "Não parece ter nada errado com o lugar apesar de ter aparecido do nada."
                s "Como você tem sorte!"
                e "(Grita assustado)"
                s "Calma, você é sortudo de fato."
                s "Escolhendo logo a comida mais importante da história."
                e "Importante porque?"
                s "Ela é uma comida regional do estado do Pará, sabia?"
                s "Ah e é a única que te dá a oportunidade de comer e aproveitar ao máximo todo o festival e sem ser envenenado."
                e "E eu deveria ficar aliviado porque se ainda preciso gastar?"
                s "Ah mas tem uma vantagem: a comida é de graça."
                e "(Olha em volta sorrindo)."
                h "Música boa tocando, comida que felizmente não o fazia passar mal ou coisa pior."
                h "Foi com muita alegria e disposição  que aproveitou o resto da noite dançando mesmo que sozinho com seu prato cheio de quitutes feitos de mandioca."
                h "Estava quase soltando o botão da calça para aliviar a barriga quando viu um rapaz dizendo em voz baixa."
                jump rapaz
            
             "Mandioca frita é o meu preferido. Quero com certeza!":
                scene mandiocafrita
                show mandiocafrita at truecenter:
                    zoom 1
                with dissolve

                e "(Morde com vontade mas do nada vem um gosto muito forte e esquisito.)"
                e "(Sua boca começa a formigar e ficar mole. Tem suadouros e sua visão vai ficando preta. Você vê um vulto branco chegando perto de você.)"
                scene fundopreto
                show fundopreto at truecenter:
                    zoom 1
                with dissolve

                s " Eu disse e você me ignorou totalmente."
                s " NÃO DEVIA COMER NADA QUE TE OFERECESSEM!"
                s "Tudo envenenado. (Suspira)"
                s "Mas vou te dar mais uma chance. Vou te mandar de novo pro início e dessa vez me escute em!"
                jump start

             "É melhor não. Meu estômago não está bom depois de ter comido a um tempo atrás.": 
                c "Entendo, mas que pena não poder aproveitar."
                c "Bom que ainda tem a música. Mais lá na frente tá tendo um show bem animado."
                c "Aproveite o festival e boas festas."
                
                scene fest
                show fest at truecenter:
                   zoom 1
                with dissolve
                
                h "Clara vai embora e você começa a andar por entre as barracas olhando as comidas, e recusando-as quando lhe oferecem."
                h "A música era contagiante."
                h "Dançou com os que estavam ali na pista e fez par com mais de uma pessoa."
                h "Não sabia dançar tão bem quanto as pessoas ali, porém se divertiu até que suas pernas se cansaram e a fome começou a bater."
                e "Estava quase se sentando num banco próximo quando viu um rapaz dizendo em voz baixa."
                jump rapaz

label rapaz:
    scene rapaz
    show rapaz at truecenter:
        zoom 1
    with dissolve
    r "Bolinho de mandioca."
    r "Bolinhos... Alguém quer?"
    r "Alguém?"
    r "Oi, você quer experimentar meus bolinhos de mandioca?"
    r "São simples e tudo mais, eu vou entender se não quiser experimentar, mas quer experimentar?"
    h "Ele te olha com uma cara esperançosa."

    menu:
                        "É melhor não, eu não consigo mais comer hoje.":
                            r "Ele te olha pra baixo cabisbaixo e desaparece dentro do estande."
                            h "Você aproveita pra dar mais uma volta vendo os outros estandes para fazer a digestão."
                            h "Tinha comido tanta coisa. Quem sabe depois de um tempo conseguisse algum lugar para comer a comida que o levaria para casa."
                            e "Ainda não passei em todas as barracas..."
                            h "Ao dar a segunda volta você percebe algo estranho."
                            h "A barraca de bolinhos de mandioca não estava mais ali."
                            h "Você roda o espaço mais uma vez olhando atentamente ao seu redor."
                            e "Pra onde foi?"
                            s "Não adianta, não está mais ali, você perdeu sua chance quando recusou da primeira vez."
                            e "Era a comida que me levava pra casa? E como eu saio daqui agora? Porque não tem trem, não tem ônibus e não parece ter uma rua que vá a qualquer lugar."
                            s "Não tem."
                            s "Você só vai reviver esse dia eternamente."
                            s "Pelo menos você pode comer as comidas daqui agora. Até mais."
                            e "O que? Espera!"
                            s "Desejo sorte para aguentar os próximos anos até alguém aparecer aqui novamente, só assim a barraca vai aparecer mais uma vez."
                            jump fimdejogot

                        "Não vou fazer essa desfeita, né. Claro que vou comer.":
                            e "(Mastiga, mastiga e mastiga e percebe ser o melhor prato de comida que já provou naquela noite.)"
                            e "É muito bom. De simples tem é nada. Tua receita é a melhor de todas!"
                            r "(Sorri e de repente tudo começa a desaparecer ao seu redor.)"
                            s "É hora de voltar pra casa. Ou quase. Boa viagem de volta e nos vemos qualquer dia desses... ou não."
                            
                            stop music

                            play music "audio/trem.mp3"

                            scene tremfim
                            show tremfim at truecenter:
                            with dissolve

                            h "(Você abre seus olhos e vê o vagão do trem que estava lotado de pessoas.)"
                            l "Próxima estação Osasco."
                            e "Ao desembarcar, cuidado com o ovão entre o trem e a plataforma."
                            e "Bem vindo a fantástica cidade de oz."
                            h "(menino puxando a mãe esbarra em você)"
                            
                            play music "audio/pru.mp3"

                            h "A cidade dos pombo, mãe. Pru pru. Olha, voou."
                            jump fimdejogob

label fimdejogot:
    
    stop music

    scene fundopreto
    show fundopreto at truecenter:
        zoom 1
    with dissolve

    s "Obrigada por jogar e boa sorte na próxima. Esse é o É Tudo Mandioca!"
    s "Ah e não se esqueçam de aplaudir de pé e dar muita mandioca para nossas guerreiras, Azuri no roteiro e pesquisa e Mei por severino-Quer dizer, programação!!!"
return

label fimdejogob:
    

    s "Parabéns por ter conseguido sair! Obrigada por jogar. Esse é o É Tudo Mandioca!"
    s "Ah e não se esqueçam de aplaudir de pé e dar muita mandioca para nossas guerreiras, Azuri no roteiro e pesquisa e Mei por severino-Quer dizer, programação!!!"
return

        