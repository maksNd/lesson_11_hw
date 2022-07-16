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
    candidates_by_name = get_candidates_by_quality(candidate_name, 'name')
    if candidates_by_name:
        candidates_count = len(candidates_by_name)
        return render_template('by_name.html', candidates_count=candidates_count, candidates=candidates_by_name)
    else:
        return render_template('if_name_not_found.html', candidate_name=candidate_name)


@app.route('/skill/<skill_name>')
def show_candidate_with_skill(skill_name):
    candidates_by_skill = get_candidates_by_quality(skill_name, 'skills')
    if candidates_by_skill:
        candidates_count = len(candidates_by_skill)
        return render_template('skill.html', candidates=candidates_by_skill, skill_name=skill_name,
                               candidates_count=candidates_count)
    else:
        return render_template('if_skill_not_found.html', skill_name=skill_name)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888)
