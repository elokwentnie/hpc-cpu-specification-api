"""
Script to update existing database records with codenames.

This script updates all existing CPU records in the database by automatically
determining their codename (Naples, Rome, Milan, etc.) based on model and launch year.
"""

from database import SessionLocal, CPUSpec
from utils import determine_cpu_generation


def update_all_codenames():
    """Update codename field for all CPUs in the database"""
    db = SessionLocal()
    try:
        cpus = db.query(CPUSpec).all()
        updated_count = 0
        
        for cpu in cpus:
            if not cpu.codename and cpu.cpu_model and cpu.launch_year:
                codename = determine_cpu_generation(
                    cpu.cpu_model, 
                    cpu.launch_year, 
                    cpu.family
                )
                if codename:
                    cpu.codename = codename
                    updated_count += 1
        
        db.commit()
        print(f"✅ Updated {updated_count} CPU records with codenames")
        print(f"📊 Total CPUs in database: {len(cpus)}")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error updating codenames: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    print("🔄 Updating codenames for all CPUs...")
    update_all_codenames()
    print("✨ Update complete!")

