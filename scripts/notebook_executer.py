import os
import argparse
import glob
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError

# print(os.name)
# print(os.path.normpath('a\\b'))
# Parse args
parser = argparse.ArgumentParser(description="Runs a set of modelling notebooks.")
file_text = """ Notebook file(s) to be run, e.g. '*.ipynb' (default),
'my_nb1.ipynb', 'my_nb1.ipynb my_nb2.ipynb', 'my_dir/*.ipynb'
"""
parser.add_argument('file_list', metavar='F', type=str, nargs='*',
    help=file_text)
parser.add_argument('-t', '--timeout', help='Length of time (in secs) a cell \
    can run before raising TimeoutError (default 800).', default=1800,
    required=False)
parser.add_argument('-p', '--run-path', help='The path of the notebook will be \
    run from (default pwd).', default=os.path.normpath(f'..{os.sep}notebook{os.sep}modelling{os.sep}'), required=False)
args = parser.parse_args()
print('Args:', args)

fl_path = f"..{os.path.sep}notebook{os.path.sep}modelling{os.path.sep}02_Fast_Hyperopt_Sales_Subspace_Search_Curves.ipynb"
if not args.file_list: # Default file_list
    args.file_list = glob.glob(fl_path)
# # Check list of notebooks
sequences=['01_seasonality_nonmedia_selection',
           '02_Fast_Hyperopt_Sales_Subspace_Search_Curves',
           '03_SliderTechniqueModel',
           '04_Model_Units',
           '05_Model_Customer',
           '06_simulator_notebook',
           '07_optimizer_notebook',
           '08_joint_optimizer_notebook',
           '09_generate_S_curve_graphs',
           '10_model_documentation',
           '11_model_insights_deck_input_automation'
           ]
notebooks = []


print('Notebooks to run:')
for f in args.file_list:
    # Find notebooks but not notebooks previously output from this script
    if f.endswith('.ipynb') and not f.endswith('_out.ipynb'):
        print(f[:-6])
        notebooks.append(f[:-6]) # Want the filename without '.ipynb'
new_seq=[]
for sq in sequences:
    for fl in notebooks:
        if fl.endswith(sq):
            new_seq.append(fl)
            break
# Execute notebooks and output


num_notebooks = len(new_seq)
print('*****')
for i, n in enumerate(new_seq):
    print("==>")
    print(n)

    op=n.split(os.path.normpath(os.sep))[:-1]
    op.append('notebooks_output')
    op=os.path.normpath(os.sep).join(op)

    if not os.path.exists(op):
        os.makedirs(op)
    n_out = f'{n}_out'
    with open(f'{n}.ipynb') as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=int(args.timeout), kernel_name='python3')
        try:
            print('Running', n, ':', i, '/', num_notebooks)
            out = ep.preprocess(nb, {'metadata': {'path': args.run_path}})
        except CellExecutionError:
            out = None
            msg = 'Error executing the notebook "%s".\n' % n
            msg += 'See notebook "%s" for the traceback.' % n_out
            print(msg)
        except TimeoutError:
            msg = 'Timeout executing the notebook "%s".\n' % n
            print(msg)
        finally:
            # Write output file
            lst = n_out.split(os.path.normpath(os.sep))
            lst.insert(-1,"notebooks_output")
            n_out=os.path.normpath(os.sep).join(lst)
            with open(f'{n_out}.ipynb', mode='wt') as f:
                nbformat.write(nb, f)
