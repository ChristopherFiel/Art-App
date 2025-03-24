screen gallery_navigation:
    vbox:
        spacing 20
        xoffset -100
        textbutton "General" action ShowMenu("galleryA")
        textbutton "Cecily" action ShowMenu("galleryB")
        textbutton "Colette" action ShowMenu("galleryC")
        textbutton "Calille" action ShowMenu("galleryD")

        textbutton "Return" action Return() yoffset 200
