import { useEffect, useState } from "react"
import api from "../../api"
import Build from "../../components/Build/Build"

function Home(){
    const [builds, setBuilds] = useState([])

    useEffect(()=>{
        api.get("/builds/")
        .then((resp) => setBuilds(resp.data))
        .catch((error) => console.log(`ERRO ${error}`))
    }, [])


    return(
        <div className="home-main">
            {builds.map((value) => {
                return(
                    <div key={value.id}>
                        <Build
                            id={value.id}
                            classe={value.classe}
                            nome={value.nome}

                            topo_1={value.topo_1}
                            topo_2={value.topo_2}
                            topo_3={value.topo_3}
                            armadura={value.armadura}
                            mao_direita={value.mao_direita}
                            mao_esquerda={value.mao_esquerda}
                            capa={value.capa}
                            sapato={value.sapato}
                            acessorio_1={value.acessorio_1}
                            acessorio_2={value.acessorio_2}

                            forca={value.forca}
                            agilidade={value.agilidade}
                            vitalidade={value.vitalidade}
                            inteligencia={value.inteligencia}
                            destreza={value.destreza}
                            sorte={value.sorte}

                            observacoes={value.observacoes}
                        />
                    </div>
                )

            })}
        </div>
    )
}

export default Home