from flask import Flask, render_template
from utils import load_candidates, get_candidate_by_id, get_candidates_by_quality

app = Flask(__name__)


@app.route('/')
def show_all_candidates():
    candidates = load_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def show_candidate_by_pk(x):
    candidate = get_candidate_by_id(x)
    return render_template('by_id.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def show_candidate_by_name(candidate_name):
    candidates = get_candidates_by_quality(candidate_name, 'name')
    candidates_count = len(candidates)
    return render_template('by_name.html', candidates_count=candidates_count, candidates=candidates)


@app.route('/skill/<skill_name>')
def show_candidate_with_skill(skill_name):
    candidates = get_candidates_by_quality(skill_name, 'skills')
    candidates_count = len(candidates)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name,
                           candidates_count=candidates_count)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)
