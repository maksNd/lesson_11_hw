from flask import Flask, render_template
from utils import load_candidates, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

list_with_all_candidates = load_candidates()


@app.route('/')
def show_all_candidates():
    candidates = list_with_all_candidates
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:x>')
def show_candidate_by_pk(x):
    candidate = get_candidate_by_id(x)
    return render_template('by_id.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def show_candidate_by_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_count = len(candidates)
    return render_template('by_name.html', candidates_count=candidates_count, candidates=candidates)


@app.route('/skill/<skill_name>')
def show_candidate_with_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_count = len(candidates)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name,
                           candidates_count=candidates_count)


app.run(host='127.0.0.1', port=8888)
