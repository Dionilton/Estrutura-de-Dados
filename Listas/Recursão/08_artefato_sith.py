def buscarArtefato():
    if type(bb8.verificarChao()) == tuple:
        return bb8.verificarChao()
    else:
        if bb8.verificarNorte():
            bb8.moverNorte()
            if not bb8.verificarSeFoiVisitado():
                bb8.registrarComoVisitado()
                buscarArtefato()
            
        if bb8.verificarSul():
            bb8.moverSul()
            if not bb8.verificarSeFoiVisitado():
                bb8.registrarComoVisitado()
                buscarArtefato()
            
        if bb8.verificarLeste():
            bb8.moverLeste()
            if not bb8.verificarSeFoiVisitado():
                bb8.registrarComoVisitado()
                buscarArtefato()
            
        if bb8.verificarOeste():
            bb8.moverOeste()
            if not bb8.verificarSeFoiVisitado():
                bb8.registrarComoVisitado()
                buscarArtefato()