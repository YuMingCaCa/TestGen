import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_figure_1_cfg():
    """Vẽ hình 1: Minh họa chuyển đổi từ XACML Tree sang CFG"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # --- Phần trái: XACML Tree ---
    ax1.set_title("(a) Cấu trúc cây XACML (Tree)", fontsize=12, pad=10)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    # Nodes
    props = dict(boxstyle='round', facecolor='white', edgecolor='black')
    ax1.text(5, 9, "PolicySet", ha='center', va='center', bbox=props, fontweight='bold')
    ax1.text(3, 6, "Policy 1", ha='center', va='center', bbox=props)
    ax1.text(7, 6, "Policy 2", ha='center', va='center', bbox=props)
    ax1.text(2, 3, "Rule 1.1", ha='center', va='center', bbox=props)
    ax1.text(4, 3, "Rule 1.2", ha='center', va='center', bbox=props)
    
    # Edges
    ax1.plot([5, 3], [8.5, 6.5], 'k-')
    ax1.plot([5, 7], [8.5, 6.5], 'k-')
    ax1.plot([3, 2], [5.5, 3.5], 'k-')
    ax1.plot([3, 4], [5.5, 3.5], 'k-')

    # --- Phần phải: CFG ---
    ax2.set_title("(b) Đồ thị luồng điều khiển (CFG)", fontsize=12, pad=10)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')

    # Nodes CFG (Start -> Decision -> End)
    props_diamond = dict(boxstyle='darrow', facecolor='#e6f2ff', edgecolor='black') # Decision node
    props_circle = dict(boxstyle='circle', facecolor='#ffe6e6', edgecolor='black') # End node
    
    ax2.text(5, 9, "Start", ha='center', va='center', bbox=dict(boxstyle='round', facecolor='#ccffcc'))
    ax2.text(5, 6.5, "Check\nTarget", ha='center', va='center', bbox=props, fontsize=9)
    ax2.text(5, 4, "Combine\nRules", ha='center', va='center', bbox=props_diamond, fontsize=9)
    ax2.text(2, 1.5, "Permit", ha='center', va='center', bbox=props_circle)
    ax2.text(8, 1.5, "Deny", ha='center', va='center', bbox=props_circle)

    # Edges CFG
    ax2.arrow(5, 8.5, 0, -1.2, head_width=0.3, head_length=0.3, fc='k', ec='k')
    ax2.arrow(5, 5.8, 0, -1.0, head_width=0.3, head_length=0.3, fc='k', ec='k')
    ax2.arrow(4.2, 3.5, -1.8, -1.3, head_width=0.3, head_length=0.3, fc='k', ec='k')
    ax2.text(3, 2.5, "True", fontsize=8, color='green')
    ax2.arrow(5.8, 3.5, 1.8, -1.3, head_width=0.3, head_length=0.3, fc='k', ec='k')
    ax2.text(7, 2.5, "False", fontsize=8, color='red')

    plt.tight_layout()
    plt.savefig('fig1_cfg.png', dpi=300)
    print("Đã tạo fig1_cfg.png")

def create_figure_2_ga_workflow():
    """Vẽ hình 2: Lưu đồ giải thuật di truyền"""
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    box_props = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black')
    
    # Các bước
    steps = [
        (5, 11, "Start", '#ccffcc'),
        (5, 9.5, "1. Initialize Population\n(Binary encoding)", 'white'),
        (5, 8, "2. Evaluate Fitness\n(Coverage & Size)", 'white'),
        (5, 6.5, "3. Selection\n(Tournament)", 'white'),
        (5, 5, "4. Crossover & Mutation", 'white'),
        (5, 3.5, "Stop Condition Met?", '#fff2cc'), # Diamond shape simulation
        (5, 1.5, "Output Optimal\nTest Suite", '#ffcccc')
    ]
    
    for x, y, text, color in steps:
        style = 'round,pad=0.5' if "?" not in text else 'darrow,pad=0.3'
        ax.text(x, y, text, ha='center', va='center', 
                bbox=dict(boxstyle=style, facecolor=color, edgecolor='black'), fontsize=11)
        
    # Mũi tên nối
    ax.arrow(5, 10.6, 0, -0.6, head_width=0.2, fc='k', ec='k') # Start -> Init
    ax.arrow(5, 9.0, 0, -0.5, head_width=0.2, fc='k', ec='k')  # Init -> Eval
    ax.arrow(5, 7.5, 0, -0.5, head_width=0.2, fc='k', ec='k')  # Eval -> Sel
    ax.arrow(5, 6.0, 0, -0.5, head_width=0.2, fc='k', ec='k')  # Sel -> Cross
    ax.arrow(5, 4.5, 0, -0.5, head_width=0.2, fc='k', ec='k')  # Cross -> Stop
    
    # Mũi tên điều kiện Stop
    ax.text(5.2, 2.6, "Yes", fontsize=10)
    ax.arrow(5, 2.9, 0, -0.8, head_width=0.2, fc='k', ec='k') # Yes -> End
    
    # Mũi tên Loop (No)
    ax.text(7.5, 3.5, "No (Next Gen)", fontsize=10)
    ax.plot([6.5, 8.5], [3.5, 3.5], 'k-') # Ngang ra phải
    ax.plot([8.5, 8.5], [3.5, 8], 'k-')   # Lên trên
    ax.arrow(8.5, 8, -2.4, 0, head_width=0.2, fc='k', ec='k') # Quay lại Eval
    
    plt.title("Genetic Algorithm Optimization Workflow", fontsize=14)
    plt.tight_layout()
    plt.savefig('fig2_ga.png', dpi=300)
    print("Đã tạo fig2_ga.png")

def create_figure_3_chart():
    """Vẽ hình 3: Biểu đồ so sánh kết quả"""
    datasets = ['HACS', 'FMS', 'SIS', 'Average']
    all_paths = [40, 55, 35, 43.3]
    ga_optimal = [18, 22, 15, 18.3]

    x = np.arange(len(datasets))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, all_paths, width, label='Graph Traversal (All Paths)', color='#a6cee3')
    rects2 = ax.bar(x + width/2, ga_optimal, width, label='GA Optimized (Proposed)', color='#1f78b4')

    ax.set_ylabel('Number of Test Cases')
    ax.set_title('Test Suite Reduction Analysis')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend()

    # Thêm số liệu lên cột
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    plt.tight_layout()
    plt.savefig('fig3_chart.png', dpi=300)
    print("Đã tạo fig3_chart.png")

if __name__ == "__main__":
    create_figure_1_cfg()
    create_figure_2_ga_workflow()
    create_figure_3_chart()