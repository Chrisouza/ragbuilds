import "./Build.css"


function Build(props){
    const showObservacoes = (e) => {
        e.preventDefault()
    }



    const icon_classe = `https://ik.imagekit.io/g9rjw1x4xiv/RagStores/assets/costume/job/icon_jobs_${props.classe.idClasse}.png`
    const img_classe = props.classe.img_path
    const links = [
        `https://ragstores.com/search/${props.topo_1.idItem}`,
        `https://ragstores.com/search/${props.topo_2.idItem}`,
        `https://ragstores.com/search/${props.topo_3.idItem}`,
        `https://ragstores.com/search/${props.armadura.idItem}`,
        `https://ragstores.com/search/${props.mao_direita.idItem}`,
        `https://ragstores.com/search/${props.mao_esquerda.idItem}`,
        `https://ragstores.com/search/${props.capa.idItem}`,
        `https://ragstores.com/search/${props.sapato.idItem}`,
        `https://ragstores.com/search/${props.acessorio_1.idItem}`,
        `https://ragstores.com/search/${props.acessorio_2.idItem}`
    ]

    return(
        <section className="build_main">
            <div className="nome_build">
                <span className="classe_icon">
                    <img src={icon_classe} alt="icone da classe" />
                </span>
                {props.nome}
            </div>
            <div className="equips">
                <table>
                    <tr>
                        <td>
                            <a href={links[0]} target="_blank" referrerPolicy="no-referrer">
                                {props.topo_1.nome}
                            </a>
                        </td>
                        <td rowSpan={5}>
                            <img src={img_classe} alt="" />
                        </td>
                        <td colSpan={2}>
                            <a href={links[1]} target="_blank" referrerPolicy="no-referrer">
                                {props.topo_2.nome}
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href={links[2]} target="_blank" referrerPolicy="no-referrer">
                                {props.topo_3.nome}
                            </a>
                        </td>
                        <td colSpan={2}>
                            <a href={links[3]} target="_blank" referrerPolicy="no-referrer">
                                {props.armadura.nome}
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href={links[4]} target="_blank" referrerPolicy="no-referrer">
                                {props.mao_direita.nome}
                            </a>
                        </td>
                        <td colSpan={2}>
                            <a href={links[5]} target="_blank" referrerPolicy="no-referrer">
                                {props.mao_esquerda.nome}
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href={links[6]} target="_blank" referrerPolicy="no-referrer">
                                {props.capa.nome}
                            </a>
                        </td>
                        <td colSpan={2}>
                            <a href={links[7]} target="_blank" referrerPolicy="no-referrer">
                                {props.sapato.nome}
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <a href={links[8]} target="_blank" referrerPolicy="no-referrer">
                                {props.acessorio_1.nome}
                            </a>
                        </td>
                        <td colSpan={2}>
                            <a href={links[9]} target="_blank" referrerPolicy="no-referrer">
                                {props.acessorio_2.nome}
                            </a>
                        </td>
                    </tr>

                </table>
            </div>

            <div className="atributos">
                <table>
                <tr>
                        <td>FOR: {props.forca}</td>
                        <td>AGI: {props.agilidade}</td>
                        <td>VIT: {props.vitalidade}</td>
                    </tr>
                    <tr>
                        <td>INT: {props.inteligencia}</td>
                        <td>DES: {props.destreza}</td>
                        <td>SOR: {props.sorte}</td>
                    </tr>
                </table>
            </div>
            <div className="buttons">
                <button onClick={showObservacoes}>Ver observacoes</button>
            </div>
            <div className="show_observacoes">
                {props.observacoes}
            </div>
        </section>
    )
}

export default Build