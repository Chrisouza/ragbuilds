module.exports = app => {
    const jobsDB = app.data.jobs
    const controller = {}
    controller.listjobs = (req, res) => res.status(200).json(jobsDB)
    return controller
}