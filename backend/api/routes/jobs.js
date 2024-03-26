module.exports = app => {
    const controller = app.controllers.jobs
    app.route('/api/v1/jobs/').get(controller.listjobs)
}