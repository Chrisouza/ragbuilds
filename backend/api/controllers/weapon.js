module.exports = app => {
    const weaponDB = app.data.weapons
    const controller = {}
    controller.listweapons = (req, res) => res.status(200).json(weaponDB)
    return controller
}